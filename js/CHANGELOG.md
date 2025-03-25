# Changelog

## [1.1.0](https://github.com/shaneholloman/dotprompt/compare/dotprompt-v1.0.1...dotprompt-v1.1.0) (2025-03-25)


### Features

* add implementation of helpers and util modules; move interfaces into dotpromptz project ([#73](https://github.com/shaneholloman/dotprompt/issues/73)) ([8c7aea1](https://github.com/shaneholloman/dotprompt/commit/8c7aea1faffaf823d01b132e55cb175a4fca5ccb))
* adds renderMetadata method to render metadata without prompt inputs ([#11](https://github.com/shaneholloman/dotprompt/issues/11)) ([7706cb7](https://github.com/shaneholloman/dotprompt/commit/7706cb7e6bce0fede5c8e2f2285be8f9aa3230ab))
* **go/parse:** parse.go implementation [#62](https://github.com/shaneholloman/dotprompt/issues/62) ([#87](https://github.com/shaneholloman/dotprompt/issues/87)) ([d5dc13c](https://github.com/shaneholloman/dotprompt/commit/d5dc13c0bf0437875a3b133511ffed474a8b3bf9))
* parseDocument python ([#80](https://github.com/shaneholloman/dotprompt/issues/80)) ([82ebc36](https://github.com/shaneholloman/dotprompt/commit/82ebc3672e8de051dfbdd92968ed3f84c79a247f))
* partial test runner implementation now loads tests ([#139](https://github.com/shaneholloman/dotprompt/issues/139)) ([b09dd2f](https://github.com/shaneholloman/dotprompt/commit/b09dd2f9b8029317ce484d6f32d5a3fb89f5f7e1))
* **py:** implement identify_partials in terms of regexps since we do not have an AST to walk [#90](https://github.com/shaneholloman/dotprompt/issues/90) ([#150](https://github.com/shaneholloman/dotprompt/issues/150)) ([f802275](https://github.com/shaneholloman/dotprompt/commit/f8022755d7eef716bbb54dd08a2c3a061250d393))
* **py:** implementation of parse.py; refactor parse.ts and update tests. ([#79](https://github.com/shaneholloman/dotprompt/issues/79)) ([47e7245](https://github.com/shaneholloman/dotprompt/commit/47e7245c0aae710b102178019d1f3449c2f1af66))
* **python:** add OpenAI adapter implementation for dotprompt [#38](https://github.com/shaneholloman/dotprompt/issues/38) ([#97](https://github.com/shaneholloman/dotprompt/issues/97)) ([d171f87](https://github.com/shaneholloman/dotprompt/commit/d171f8792ecf08f446e18ea3bbd5309cafa1d8a3))
* script to update all deps in one go and update deps ([#130](https://github.com/shaneholloman/dotprompt/issues/130)) ([09ac58e](https://github.com/shaneholloman/dotprompt/commit/09ac58e4512fae817a63f731ac0db80967842436))


### Bug Fixes

* changed handlebars import to fix downstream libCheck errors ([#18](https://github.com/shaneholloman/dotprompt/issues/18)) ([c43bf8d](https://github.com/shaneholloman/dotprompt/commit/c43bf8d83c81a6a61421c95ebba7a733e9ebc4e4))
* **deps:** switch to version 1.23 of go; update pnpm deps ([#153](https://github.com/shaneholloman/dotprompt/issues/153)) ([672b8da](https://github.com/shaneholloman/dotprompt/commit/672b8da68e784abd17a14f9f1f292d9b65b88a80))
* formatting and license headers for source and commit messages [#32](https://github.com/shaneholloman/dotprompt/issues/32) ([#33](https://github.com/shaneholloman/dotprompt/issues/33)) ([4ba47de](https://github.com/shaneholloman/dotprompt/commit/4ba47de715d26e5b5abe4d4ba7210662c5894fc4))
* **go,py:** type fixes and ensure we build/lint the go code in hooks and ci ([#83](https://github.com/shaneholloman/dotprompt/issues/83)) ([19a8257](https://github.com/shaneholloman/dotprompt/commit/19a8257f4f73b776229d5324a0366fd9a79c20aa))
* **js:** an issue with loose equality for helpers; add missing tests for some helpers [#53](https://github.com/shaneholloman/dotprompt/issues/53) [#54](https://github.com/shaneholloman/dotprompt/issues/54) ([#55](https://github.com/shaneholloman/dotprompt/issues/55)) ([f645628](https://github.com/shaneholloman/dotprompt/commit/f645628a50def0b661009311ac7ed84fb358e0f0))
* **license:** use the full license header in source code ([#142](https://github.com/shaneholloman/dotprompt/issues/142)) ([64894ef](https://github.com/shaneholloman/dotprompt/commit/64894ef898876b861c6c244d522f634cd8fcc842))
* only set description on the resolve schema if available (avoid null description being set) ([#16](https://github.com/shaneholloman/dotprompt/issues/16)) ([1fc648c](https://github.com/shaneholloman/dotprompt/commit/1fc648c9834b63ff0dc36272521229abf66c0155))
