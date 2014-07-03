;
(function ($, window, document) {
  var pluginName = "EventCalendar";
  var defaults = {
    dayNames: ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'],
    monthNames: ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
  };

  function EventCalendar(element, options) {
    this.element = element;
    this.$el = $(element);
    this.options = $.extend({}, defaults, options);

    this._defaults = defaults;
    this._name = pluginName;

    this.counter = 0;

    this.currentTime = new Date();
    this.currentYear = this.currentTime.getFullYear();
    this.currentMonth = this.currentTime.getMonth();

    // the active time can be different to the current time
    // e.g. when you want to set a different start date
    this.activeTime = new Date();
    this.activeYear = this.activeTime.getFullYear();
    this.activeMonth = this.activeTime.getMonth();

    this.eventData = {};

    this.init();
  }

  EventCalendar.prototype.init = function () {
    this.drawCalendar();

    this.getEventData();
    this.setCallbacks();
  };

  EventCalendar.prototype.getEventData = function () {
    var url = '/calendar/events/' + this.activeYear + '/' + (this.activeMonth + 1) + '/';

    $.ajax({
      type: 'GET',
      url: url,
      success: $.proxy(this.updateEventData, this)
    });
  };

  EventCalendar.prototype.updateEventData = function (eventData) {
    var days = {};

    $.each(eventData, function (index, date) {
      days[date['scheduled_date']] = {
        count: date['count']
      }
    });

    this.eventData = days;
    this.drawDays();
  };

  EventCalendar.prototype.pad = function(n) {
    // http://stackoverflow.com/a/8089938
    return (n < 10) ? ("0" + n) : n;
  };

  EventCalendar.prototype.drawDays = function () {
    var day;
    var dateStr;
    var container = this.$el.find('.days');

    var firstWeekDay = new Date(this.activeYear, this.activeMonth, 0).getDay();
    var daysInMonth = new Date(this.activeYear, this.activeMonth + 1, 0).getDate();

    this.$el.find('#activeMonth').html(this.options.monthNames[this.activeMonth] + ' ' + this.activeYear);

    var futureDays = 7 - ((firstWeekDay + daysInMonth) % 7);
    if (futureDays == 7)
      futureDays = 0;

    // draw optional days from previous month
    for (var weekDay = 0; weekDay < firstWeekDay; weekDay++) {
      day = $('<div><a></a></div>');
      day.addClass("day");
      day.addClass("past");
      container.append(day);
    }

    // draw days for active month
    for (var dayCounter = 1; dayCounter <= daysInMonth; dayCounter++) {
      day = $('<div><a></a></div>');
      day.addClass("day");
      day.addClass("current");
      day.attr('data-year', this.activeYear);
      day.attr('data-month', this.activeMonth);
      day.attr('data-day', dayCounter);
      day.html(dayCounter);

      // look for events on that date
      dateStr = this.activeYear + '-' + this.pad(this.activeMonth + 1) + '-' + this.pad(dayCounter);
      if (this.eventData[dateStr] != undefined) {
        day.append('<span class="badge">' + this.eventData[dateStr].count + '</span>');
      }


      container.append(day);
    }

    // draw optional days for next month
    for (var futureCounter = 0; futureCounter < futureDays; futureCounter++) {
      day = $('<div><a></a></div>');
      day.addClass("day");
      day.addClass("future");
      container.append(day);
    }

    this.$el.find('div.current').on('click', $.proxy(this.dayClickHandler, this));
  };

  EventCalendar.prototype.drawCalendar = function () {
    this.$el.append('<a class="cta pull-left" data-go="prev-month"><i class="fa fa-angle-double-left"></i></a>');
    this.$el.append('<a class="cta pull-right" data-go="next-month"><i class="fa fa-angle-double-right"></i></a>');
    this.$el.append('<h3 id="activeMonth"></h3>');

    this.$el.append('<div class="clearfix"></div>');

    this.$el.append('<div class="headers"></div>');
    this.$el.append('<div class="days"></div>');

    for (var day = 0; day < 7; day++) {
      var day_header = $('<div>' + this.options.dayNames[day] + '</div>');
      day_header.addClass('day header');
      this.$el.find('.headers').append(day_header);
    }
  };

  EventCalendar.prototype.updateCalendar = function () {
    this.$el.find('.days').empty();
    this.drawDays();
  };

  EventCalendar.prototype.setCallbacks = function () {
    this.$el.find('[data-go="next-month"]').on('click', $.proxy(this.nextMonth, this));
    this.$el.find('[data-go="prev-month"]').on('click', $.proxy(this.previousMonth, this));
  };

  EventCalendar.prototype.dayClickHandler = function (event) {
    var target;
    var url;

    $('.active').removeClass('active');
    target = $(event.target);
    target.addClass('active');
    this.activeDay = target.attr('data-day');

    url = '/calendar/events/' + this.activeYear + '/' + (this.activeMonth + 1) + '/' + this.activeDay + '/';

    $.ajax({
      type: 'GET',
      url: url,
      success: $.proxy(this.updateEventList, this)
    });
  };

  EventCalendar.prototype.nextMonth = function () {
    if (this.activeMonth + 1 > 11) {
      this.activeYear++;
      this.activeMonth = 0;
    }
    else {
      this.activeMonth++;
    }
    this.updateCalendar();
  };

  EventCalendar.prototype.previousMonth = function () {
    if (this.activeMonth - 1 < 0) {
      this.activeYear--;
      this.activeMonth = 0;
    }
    else {
      this.activeMonth--;
    }
    this.updateCalendar();
  };

  EventCalendar.prototype.updateEventList = function (data) {
    var selector = $('#events');
    var date_selector = $('#event_date');
    var source = $('#event-template').html();
    var template = Handlebars.compile(source);

    // clear old content
    selector.html('');
    date_selector.html('');

    // add new content
    date_selector.html(this.activeDay + '.' + this.activeMonth + '.' + this.activeYear);
    $.each(data, function (index, event) {
      var html = template(event);
      selector.append(html);
    });
  };

  $.fn[pluginName] = function (options) {
    return this.each(function () {
      if (!$.data(this, "plugin_" + pluginName)) {
        $.data(this, "plugin_" + pluginName, new EventCalendar(this, options));
      }
    });
  }

})(jQuery, window, document);