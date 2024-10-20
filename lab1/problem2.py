def emails_shortener(emails):
    domain_names = {}

    for email in emails:
        name, domain = email.split("@")

        if (domain in domain_names):
            domain_names[domain].append(name)
        else:
            domain_names[domain] = [name]

    result = set()

    for domain, names in domain_names.items():
        shortened = names[0] if len(names) == 1 else f"{{{",".join(names)}}}"
        result.add(f"{shortened}@{domain}")

    return result

assert emails_shortener([
    "pesho@abv.bg", 
    "gosho@abv.bg",
    "sasho@abv.bg",
]) == {
    "{pesho,gosho,sasho}@abv.bg"
}

assert emails_shortener([
    "tinko@fmi.uni-sofia.bg", 
    "minko@fmi.uni-sofia.bg", 
    "pesho@pesho.org",
]) == {
    "{tinko,minko}@fmi.uni-sofia.bg", 
    "pesho@pesho.org",
}

assert emails_shortener([
    "toi_e@pesho.org",
    "golemiq@cyb.org",
]) == {
    "toi_e@pesho.org",
    "golemiq@cyb.org",
}

"✅ All OK! +1 points"