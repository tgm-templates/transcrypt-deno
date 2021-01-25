import {hello as py_hello} from "./__target__/main.js";

export function hello(name: string): string {
    return py_hello(name);
}