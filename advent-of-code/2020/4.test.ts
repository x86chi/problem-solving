import { readFileSync } from 'fs'
import path from 'path'

import {
  validator as generalValidator,
  parser,
  part1,
  Passport,
  Part,
  part2
} from './4'

describe('modules', () => {
  const sample: Passport = {
    ecl: 'gry',
    pid: '860033327',
    eyr: 2020,
    hcl: '#fffffd',
    byr: 1937,
    iyr: 2017,
    cid: '147',
    hgt: '183cm'
  }

  it('Parser', () => {
    const input = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm`

    expect(parser(input)).toStrictEqual(sample)
  })

  describe('validator', () => {
    const validator = generalValidator(Part.One)
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
})

describe('문제', () => {
  const sample = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in`
  describe('Part 1', () => {
    it('샘플 입력', () => {
      const input = sample
      expect(part1(input)).toBe(2)
    })

    it('정답', () => {
      const input = readFileSync(path.join(__dirname, '4.txt'), {
        encoding: 'utf8'
      })
      expect(part1(input)).toBe(250)
    })
  })
  describe('Part 2', () => {
    it('모두 유효함', () => {
      const input = `pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719`
      expect(part2(input)).toBe(4)
    })
    it('모두 유효하지 않음', () => {
      const input = `eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
`
      expect(part2(input)).toBe(0)
    })

    it('정답', () => {
      const input = readFileSync(path.join(__dirname, '4.txt'), {
        encoding: 'utf8'
      })

      expect(part2(input)).toBe(158)
    })
  })
})
