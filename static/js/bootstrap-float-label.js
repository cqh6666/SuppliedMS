(function (global, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD
        define(['jquery'], factory);
    } else if (typeof exports === 'object') {
        // CommonJS
        factory(require('jquery'));
    } else {
        // Browser globals
        factory(global.jQuery);
    }
}(this, function ($) {
    'use strict';

    var FloatingLabel = function (element, options) {
        this.$element  = $(element);
        this.$label = this.$element.find('label');
        this.$input = this.$element.find('input, textarea');

        this.options   = $.extend({}, this.getOptions(), options);

        this.$element.css('position','relative');
        this.$label.addClass(this.options.floatingLabelClass);
        this.$input.addClass(this.options.floatingInputClass);
        this.$input.attr('placeholder','');

        this.positionData = {top: parseInt(this.$input.css('padding-top')),left: parseInt(this.$input.css('padding-left'))};

        this.$label.css('position', 'absolute');
        this.$label.css('top', this.positionData.top + 'px');
        this.$label.css('left', this.positionData.left + 'px');

        var that = this;
        this.$label.on('click',function(){that.$input.focus();});
        this.$input.on('focus',function () {
            that.$label.removeClass(that.options.floatingLabelClass).addClass(that.options.floatingLabelOnClass);
            if(typeof that.$label.animate === 'function'){
                that.$label.animate({
                    top:'-' + (that.positionData.top + that.positionData.top) + 'px',
                    left: 0
                },that.options.animationDuration);
            }
            else {
                that.$label.css('top', '-' + (that.positionData.top + that.positionData.top) + 'px');
                that.$label.css('left', 0);
            }
        });
        this.$input.focusout(function () {
            if (that.$input.val().trim() === ''){
                that.$label.removeClass(that.options.floatingLabelOnClass).addClass(that.options.floatingLabelClass);
                if(typeof that.$label.animate === 'function'){
                    that.$label.animate({
                        top: that.positionData.top + 'px',
                        left: that.positionData.left + 'px'
                    },that.options.animationDuration);
                }
                else {
                    that.$label.css('top', that.positionData.top + 'px');
                    that.$label.css('left', that.positionData.left + 'px');
                }
            }
        });
    };

    FloatingLabel.prototype.getOptions = function() {
        return {
            floatingLabelClass: this.$element.attr('data-floating-label-class') || $.fn.floatingLabel.defaults.floatingLabelClass,
            floatingLabelOnClass: this.$element.attr('data-floating-label-on-class') || $.fn.floatingLabel.defaults.floatingLabelOnClass,
            floatingInputClass: this.$element.attr('data-floating-input-class') || $.fn.floatingLabel.defaults.floatingInputClass,
            animationDuration: this.$element.attr('data-animation-duration') || $.fn.floatingLabel.defaults.floatingInputClass
        };
    };

    function FloatingLabelPlugin(option) {
        return this.each(function () {
            var options = typeof option == 'object' && option;
            return new FloatingLabel(this, options);
        })
    }

    $.fn.floatingLabel             = FloatingLabelPlugin;
    $.fn.floatingLabel.Constructor = FloatingLabel;
    $.fn.floatingLabel.defaults = {
        floatingLabelClass: 'floating-label',
        floatingLabelOnClass: 'floating-label-on',
        floatingInputClass: 'floating-input',
        animationDuration: 'fast',
    };

    $(function() {
        $('.floating-control-group').floatingLabel();
    })
}));