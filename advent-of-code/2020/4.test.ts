import { readFileSync } from 'fs'
import path from 'path'

import { validator, parser, part1, Passport } from './4'

const sample: Passport = {
  ecl: 'gry',
  pid: 860033327,
  eyr: 2020,
  hcl: '#fffffd',
  byr: 1937,
  iyr: 2017,
  cid: 147,
  hgt: '183cm'
}

it('Parser', () => {
  const input = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm`

  expect(parser(input)).toStrictEqual(sample)
})

describe('validator', () => {
  it('모두 갖고 있음', () => {
    const input = sample
    expect(validator(input)).toBe(true)
  })
  it('국가 ID 만 없음', () => {
    const { cid, ...input } = sample
    expect(validator(input)).toBe(true)
  })
  it('국가 ID 외에 다른 정보도 없음', () => {
    const { cid, ecl, ...input } = sample
    expect(validator(input)).toBe(false)
  })
})

describe('Part 1', () => {
  it('sample case', () => {
    const input = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in`
    expect(part1(input)).toBe(2)
  })

  it('find answer', () => {
    const input = readFileSync(path.join(__dirname, '4.txt'), {
      encoding: 'utf8'
    })
    expect(part1(input)).toBe(250)
  })
})
