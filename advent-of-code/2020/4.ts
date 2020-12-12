export interface Passport {
  byr: number
  iyr: number
  eyr: number
  hgt: string
  hcl: string
  ecl: string
  pid: string
  cid: string
}

export enum Part {
  One,
  Two
}

const main = (part: Part) => (input: string) => {
  const passports = input.split('\n\n').map(parser)
  return passports.map(validator(part)).filter(Boolean).length
}

export const part1 = main(Part.One)
export const part2 = main(Part.Two)

const eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
const numberFields = ['byr', 'iyr', 'eyr']
const isHeightFormats = (format: string) => format === 'cm' || format === 'in'

export function validator(part: Part) {
  return function(passport: Partial<Passport>) {
    const isFieldsValid =
      !!passport.byr &&
      !!passport.iyr &&
      !!passport.eyr &&
      !!passport.hgt &&
      !!passport.hcl &&
      !!passport.ecl &&
      !!passport.pid

    if (!isFieldsValid || part === Part.One) return isFieldsValid

    const verifying = passport as Omit<Passport, 'cid'> &
      Partial<Pick<Passport, 'cid'>>

    const byr = compare(verifying.byr, 1920, 2002)
    const iyr = compare(verifying.iyr, 2010, 2020)
    const eyr = compare(verifying.eyr, 2020, 2030)

    const format = verifying.hgt.slice(-2)
    const isCm = format === 'cm'
    const hgt =
      isHeightFormats(format) &&
      compare(parseInt(verifying.hgt), isCm ? 150 : 59, isCm ? 193 : 76)

    const matched = verifying.hcl.match(/^#[0-9a-f]{6}$/)
    const hcl = matched !== null
    const ecl = eyeColors.includes(verifying.ecl)
    const pid = !isNaN(verifying.pid) && verifying.pid.length === 9
    return byr && iyr && eyr && hgt && hcl && ecl && pid
  }
}
type rawField = Record<string, string | number>

export function parser(input: string) {
  return input.split(/\s/).reduce((reducing, rawField) => {
    const [key, rawValue] = rawField.split(':')

    const field: rawField = {}

    const isNumber = numberFields.includes(key)
    const value = isNumber ? Number(rawValue) : rawValue

    field[key] = value

    return { ...reducing, ...field }
  }, {} as Passport)
}

function compare(value: number, least: number, most: number) {
  return least <= value && value <= most
}
