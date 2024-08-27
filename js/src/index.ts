import { DotpromptEnvironment, DotpromptOptions } from "./environment.js";
export * from "./types.js";
export { DotpromptOptions };

export function dotprompt(options?: DotpromptOptions): DotpromptEnvironment {
  return new DotpromptEnvironment(options);
}
