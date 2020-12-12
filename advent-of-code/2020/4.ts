export interface Passport {
  byr: number
  iyr: number
  eyr: number
  hgt: string
  hcl: string
  ecl: string
  pid: number
  cid: number
}

export function part1(input: string) {
  const passports = input.split('\n\n').map(parser)
  return passports.map(validator).filter(Boolean).length
}

export function validator(passport: Partial<Passport>) {
  return (
    !!passport.byr &&
    !!passport.iyr &&
    !!passport.eyr &&
    !!passport.hgt &&
    !!passport.hcl &&
    !!passport.ecl &&
    !!passport.pid
  )
}

type rawField = Record<string, string | number>

export function parser(input: string) {
  return input.split(/\s/).reduce((reducing, rawField) => {
    const [key, rawValue] = rawField.split(':')

    const field: rawField = {}

    const value = isNaN(rawValue) ? rawValue : Number(rawValue)

    field[key] = value

    return { ...reducing, ...field }
  }, {} as Passport)
}
