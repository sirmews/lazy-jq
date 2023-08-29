I get lazy a lot of the time and I just want to generate some quick scripts. I need something like `jq` but AI!

This is a rudimentary example.

Build with: `docker build -t jq-lazy .`
Run with `docker run -e OPEN_AI_KEY=your_key -it jq-lazy "do something" `

An example:
```sh
docker run -e OPEN_AI_KEY=your_key -it jq-lazy "can you give a simple echo statement that provides the current time" | xargs -I % bash -c '%'
```