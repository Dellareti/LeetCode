/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let initAtual = init

    return {
        increment: function(){
           initAtual += 1
           return initAtual; 
        },
        decrement: function(){
            initAtual -= 1
            return initAtual;
        },
        reset: function(){
            initAtual = init
            return init;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */