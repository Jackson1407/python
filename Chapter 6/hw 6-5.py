#Chapter 6 Homework 6-5

river = { "nile" : "egypt",
          "mississippi" : "america",
          "yangtze" : "china"
}
for k, v in river.items():
    print(f"The {k.title()} runs through {v.title()}.")