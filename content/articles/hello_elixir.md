Title: Hello Code
Date: 2010-12-20 10:20
Modified: 2010-12-20 19:30
Category:
Tags: pelican, publishing
Slug: hello-code
Authors: Marko Vukovic
Summary: Code formatting in Pelican
Status: published

Let's see how code formatting works in Pelican.

Here is some Python code:

    :::python
    print("The triple-colon syntax will *not* show line numbers.")

Here is some Elixir code:

    :::elixir
    defmodule Hello do
      def hello do
        IO.puts "Hello, world!"
      end
    end
