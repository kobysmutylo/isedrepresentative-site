---
title: ISED Certification for Industrial IoT and Smart Metering | Canadian Representative
description: What is specific about ISED certification for industrial sensors, gateways, LoRaWAN and cellular IoT, and smart utility meters: RSS-247 and RSS-210 sub-GHz, RSS-130-series cellular, module-based designs, long field lives and the Canadian Representative requirement.
h1: Industrial IoT and smart metering: ISED certification and the Canadian Representative
short: Industrial IoT and metering
type: industry
date: 2026-08-20
updated: 2026-08-20
order: 4
---

<div class="answer" markdown="1">
Industrial IoT devices and smart meters are certified under RSS-247 (2.4 GHz, 915 MHz frequency hopping and digital modulation), RSS-210 (other licence-exempt sub-GHz), and the RSS-130 family for LTE-M and NB-IoT, with RSS-102 exposure usually by exemption. Designs are module-heavy, which determines who needs a Canadian Representative. Field lives of fifteen years or more make the appointment's duration a real issue, not a formality.
</div>

## What is specific to this category

**The 902–928 MHz band.** Canada's licence-exempt 915 MHz band is harmonized with the US, and LoRaWAN, proprietary sub-GHz and many metering radios operate there under RSS-247 or RSS-210. Test data from FCC Part 15.247 work is largely reusable; see [from FCC to ISED](/guides/fcc-to-ised/). Meter-reading systems that use licensed spectrum follow their own RSS and licensing requirements with the utility.

**Modules everywhere.** A gateway typically contains a certified LoRa module, a certified cellular module and a certified Wi-Fi/BLE module. Under RSP-100 section 8 the host relies on those certifications and does not need its own unless it adds a radio or departs from the module grant conditions. The module makers, if outside Canada, need Canadian Representatives for their IC numbers; the integrator needs one only for certifications it holds. Integrators ordering letters they do not need is common in this category. See [one representative letter per IC ID](/guides/one-representative-letter-per-ic-id/).

**Field life.** Electricity, water and heat meters are installed for fifteen to twenty years and sold as replacements throughout. RSP-100 requires the Canadian Representative to be maintained for as long as the product is offered in Canada. Utilities procuring meters increasingly ask the manufacturer who its representative is and whether it will exist for the asset life. See [how long must a Canadian Representative be appointed](/guides/how-long-must-a-canadian-representative-be-appointed/). Kamstrup's metering products are an example of the category; see [clients](/clients/).

**Enterprise customers and utilities ask for the letter.** Unlike consumer products, industrial buyers often request the ISED certificate and supporting documents, including the representative letter, as part of procurement. Keep the letter in the technical file.

**Firmware-defined radios and variants.** Regional variants of the same hardware (different bands, different power) may be separate certifications or one certification with multiple HVINs; the CB decides. Letters follow the IC numbers.

## Typical certification path

RSS-247 or RSS-210 for sub-GHz and 2.4 GHz, RSS-130-series for cellular IoT, RSS-102 exemption, RSS-Gen. For gateways using only certified modules, often no new certification at all. CB issues the IC number where a certification is needed. Applicants outside Canada order the representative letter at application; we issue the same business day.

## Products we have represented

Smart electricity, water and heat meters, LoRaWAN gateways and sensors, asset trackers, industrial controllers and cellular IoT modules for manufacturers in Denmark, Germany, the United States, China and Taiwan.

<div class="source" markdown="1">
**Sources.** [RSP-100, Issue 12](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), sections 4.1, 8, 10 and 12. RSS-247, RSS-210, RSS-130 family, RSS-102 and RSS-Gen as published by ISED; confirm current issues with your lab.
</div>
