type F = (...args: number[]) => void;

function debounce(fn: F, t: number): F {
    let timeoutId: NodeJS.Timeout;

    return function(this: any, ...args: number[]) {
        clearTimeout(timeoutId);

        timeoutId = setTimeout(() => {
            fn.apply(this, args);
        }, t);
    };
}
