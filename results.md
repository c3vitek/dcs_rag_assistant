# Vyhodnocení RAG vs. holý LLM — DCS I-16

Model: `openai/gpt-4o-mini`, top-k = 4, embeddings = `all-MiniLM-L6-v2`

## [in corpus] How do I start the engine on the F-16C using the JFS?

**Očekáváno** (strany [88, 90, 91]): Engine start uses the Jet Fuel Starter (JFS). Set JFS to START2, advance throttle to IDLE around 20-25% RPM, monitor FTIT and oil pressure as the engine spools up to idle.

**RAG** (našel strany [90, 29, 146, 91]):

> To start the engine on the F-16C using the JFS (Jet Fuel Starter), follow these steps:

1. Set the ENGINE FEED Selector to NORM. This will turn on all fuel pumps and control the aircraft's CG (Centre of Gravity) (page 90).
2. Set the AIR SOURCE Selector Knob to NORM. This opens the engine bleed air valves when the engine is spooled up (page 90).
3. Verify that the throttle is at the OFF detent. You can use RSHIFT+END to set the throttle to OFF (page 90).
4. Set the JFS switch AFT to START2 (Left Click). This uses both compressed air bottles for starting if needed (page 90).
5. When the Jet Fuel Starter reaches IDLE RPM (within 30 seconds), verify that the JFS RUN green light illuminates, and the FLCS RLY and FLCS PMG lights extinguish (page 90).
6. When the JFS is operational, a clutch inside the Accessory Drive Gearbox will engage, driving the engine through the accessory drive gearbox (page 91).
7. When engine RPM reaches between 20% and 25%, move the throttle from the OFF position to the IDLE position (RSHIFT+HOME). Be cautious not to move the throttle too early to avoid a hot start or hung start (page 91).
8. The engine should light-off within 10 seconds, and engine RPM and FTIT (Fan Turbine Inlet Temperature) should increase (page 91). 

Follow these steps carefully to successfully start the engine using the JFS.

**Holý LLM** (bez příručky):

> To start the engine on the F-16C using the Jet Fuel Starter (JFS), follow these steps:

1. **Pre-Start Checks**:
   - Ensure the aircraft is in a safe condition for engine start (e.g., parking brake set, canopy closed).
   - Verify that the fuel system is configured correctly and that you have sufficient fuel.

2. **Power On**:
   - Turn on the battery switch (BAT) to provide electrical power to the aircraft systems.

3. **Engine Start Switch**:
   - Locate the Engine Start Switch on the throttle quadrant. It should be in the "OFF" position.

4. **JFS Start**:
   - Move the Engine Start Switch to the "START" position. This will engage the JFS to start the engine.
   - Monitor the RPM gauge. You should see the RPM begin to rise as the JFS starts the engine.

5. **Fuel Flow**:
   - As the RPM reaches approximately 20%, you should see fuel flow indicated on the fuel flow gauge.

6. **Engine Stabilization**:
   - Once the engine reaches idle RPM (around 60-70% RPM), you can release the Engine Start Switch back to the "NORM" position.

7. **Check Engine Parameters**:
   - Monitor the engine parameters (RPM, EGT, oil pressure) to ensure they are within normal operating ranges.

8. **Complete Start**:
   - Once the engine is stable and all parameters are normal, you can proceed with further checks and systems configurations as needed.

Remember to follow any specific procedures outlined in the F-16C flight manual or checklist for your particular mission or scenario.

**Hodnocení** (doplň ručně): citace sedí? sedí perfektně na engine start  RAG lepší? RAG byl lepší, bez ragu přeskočil mnoho kroků o kterých neměl tušení. Ale měl správné uvažování. RAG byl krásně detailní, což je přesně potřeba.  u 'mimo korpus' odmítl? nebylo třeba

---

## [in corpus] How do I align the INS before flight?

**Očekáváno** (strany [96, 97]): Set the INS knob to ALIGN NORM and wait for a full alignment (typically ~8 minutes); the DED shows the alignment status/quality before switching to NAV.

**RAG** (našel strany [97, 96, 99, 98]):

> To align the INS (Inertial Navigation System) before flight, follow these steps:

1. **Set the INS Selector Switch**: Choose either a Normal alignment or a Stored Heading alignment.
   - For Normal alignment, set the switch to **ALIGN NORM** (takes roughly 8 minutes).
   - For Stored Heading alignment, set the switch to **ALIGN STOR HDG** (takes roughly 90 seconds) (page 96).

2. **Enter Aircraft Coordinates**: 
   - Enter or confirm the latitude and longitude coordinates of your aircraft on the INS DED page within two minutes after starting an alignment. Failing to do this will result in a degraded INS alignment (page 97).
   - Check the aircraft coordinates via the F10 map and ensure they are in Degrees, Minute, Decimal-Minutes format (page 97).

3. **Confirm Coordinates**: 
   - Ensure the coordinates entered match the aircraft coordinates. Press the **ENTR** button on the ICP to enter/confirm LATITUDE coordinates, then select the LNG field (page 97).

4. **Monitor Alignment Status**: 
   - Wait for the INS Alignment Status to reach **“10 RDY”**, which indicates that the INS alignment is complete (page 98).

5. **Set to Navigation**: Once alignment is complete, set the INS Selector Switch to **NAV** (Navigation) (page 99). 

Make sure to follow these steps carefully to ensure proper INS alignment before flight.

**Holý LLM** (bez příručky):

> To align the Inertial Navigation System (INS) in the F-16C Viper before flight in DCS, follow these steps:

1. **Power Up the Aircraft**: Ensure that the aircraft is powered on. You can do this by turning on the battery and the external power if available.

2. **Set the INS Mode**: On the UFC (Up Front Control), press the `INS` button to access the INS settings.

3. **Select the Alignment Mode**: Use the UFC to select the alignment mode. You typically want to set it to "NAV" mode for normal operations. This is done by pressing the `NAV` button on the UFC.

4. **Enter the Position**: You need to enter your current position (latitude and longitude) into the INS. This can be done using the UFC. Input your coordinates in the format required (usually degrees and minutes).

5. **Start the Alignment**: Once the position is entered, press the `ALIGN` button on the UFC to start the alignment process. The alignment process will take a few minutes (typically around 5 minutes) to complete.

6. **Monitor the Alignment Status**: During the alignment, you can monitor the status on the HUD or the INS display. It will indicate when the alignment is complete.

7. **Check for Completion**: Once the alignment is complete, the INS will indicate that it is ready for navigation. You can now proceed with your pre-flight checks and takeoff.

Remember that the INS alignment is crucial for accurate navigation, so ensure that you enter the correct position and allow sufficient time for the alignment to complete before taxiing.

**Hodnocení** (doplň ručně): citace sedí? ano sedí skvěle  RAG lepší? RAG je lepší, ale bez RAG to trefil také dobře - neměl přesný čas pro alignment  u 'mimo korpus' odmítl? zde netřeba

---

## [in corpus] What is the maximum G limit of the F-16C?

**Očekáváno** (strany [154]): Around 9 G; the FLCS limits the airframe, with lower limits at heavy gross weight / with stores.

**RAG** (našel strany [7, 666, 5, 6]):

> The maximum G limit of the F-16C varies depending on the configuration mode and the angle of attack (AoA). In CAT I (Air-to-Air configuration), the FCS limits aircraft acceleration from -3 G to +9 G until 15 deg AoA is reached. Above 15 deg AoA, the maximum G is a function of AoA and airspeed, with a maximum of +7.3 G at 20 deg AoA and +1 G at 25 deg AoA. In CAT III (Air-to-Ground configuration), the FCS limits aircraft acceleration from -3 G to +9 G until 15 deg AoA is reached, and the maximum AoA is limited to 15.5 - 15.8 deg (page 666).

**Holý LLM** (bez příručky):

> The maximum G limit of the F-16C Viper is typically around +9 Gs in clean configuration (without external stores). However, this limit can vary depending on the specific configuration, weight, and other factors. It's important to consult the aircraft's flight manual or specific documentation for precise limits under different conditions.

**Hodnocení** (doplň ručně): citace sedí? dal jiné strany, ale probírá se na různých místech.  RAG lepší? oba vědely, ale rag je daleko detailnější a uvádí konkrétnější informace  u 'mimo korpus' odmítl? netřeba

---

## [in corpus] At what speed should I take off / rotate?

**Očekáváno** (strany [123]): Takeoff at approx. 173 kts; begin rotation roughly 10 kts below takeoff speed (around 160-163 kts).

**RAG** (našel strany [123, 744, 746, 416]):

> Your takeoff speed for a takeoff weight of approximately 34,000 lbs is approximately 173 kts. You should gently pull back on the stick and establish a takeoff attitude at around 10 kts below the takeoff speed, which would be approximately 163 kts in this case (page 123).

**Holý LLM** (bez příručky):

> For the F-16C Viper, the recommended rotation speed (Vr) for takeoff typically ranges between 130 to 150 knots, depending on the aircraft's weight, configuration, and environmental conditions. 

A good rule of thumb is to refer to the aircraft's weight and the specific takeoff performance charts in the flight manual or the aircraft's operating handbook for precise values. Always ensure you are aware of the current weight, fuel load, and any external stores, as these factors will influence your takeoff speed. 

Make sure to maintain a positive climb rate after rotation and follow the appropriate climb-out procedures.

**Hodnocení** (doplň ručně): citace sedí? sedí + další stránky, kde se řeší  RAG lepší? rag zminuje konkretní hodnoty pro konkretni hmotnost, hole llm to lehce podstrelilo, ale uznalo, že závisí na hmostnosti.  u 'mimo korpus' odmítl? netřeba

---

## [in corpus] What does the Master Caution light mean and how do I reset it?

**Očekáváno** (strany [35]): It signals a caution; check the caution panel for the specific warning, then press the Master Caution button to reset the light.

**RAG** (našel strany [597, 112, 35, 22]):

> The Master Caution light indicates that there is a fault that requires attention. To reset it, you need to press the Master Caution Light (Push to Reset) button (page 35).

**Holý LLM** (bez příručky):

> In the F-16C Viper, the Master Caution light indicates that there is a system fault or warning that requires your attention. This light will illuminate when any of the aircraft's systems detect a malfunction or when certain conditions are met that require the pilot to be aware of a potential issue.

To reset the Master Caution light, you can follow these steps:

1. **Identify the Warning**: First, check the warning lights and the caution messages on the DED (Data Entry Display) or the MFD (Multi-Function Display) to determine the specific issue that triggered the Master Caution.

2. **Address the Issue**: If the warning is related to a system malfunction, take the necessary actions to resolve the issue as per the aircraft's operating procedures.

3. **Reset the Master Caution**: Once the issue has been addressed, you can reset the Master Caution light by pressing the Master Caution reset button, which is typically located on the front of the throttle or on the instrument panel.

After pressing the reset button, the Master Caution light should extinguish if all issues have been resolved. If it remains illuminated, further investigation into the system faults is required.

**Hodnocení** (doplň ručně): citace sedí? sedí  RAG lepší? bez dává víc informací okolo (udělej i check těch věcí), trochu nepřesně pojmenoval to tlačítko. RAG to řekl, dobře, že zmáčkneš to světlo přímo, ale není to špatně ani u jednoho.  u 'mimo korpus' odmítl? netřeba

---

## [in corpus] How do I switch the radar between RWS and TWS modes?

**Očekáváno** (strany [173, 176]): Use the OSB next to the radar mode label on the FCR page to cycle the air-to-air mode between RWS and TWS.

**RAG** (našel strany [197, 186, 556, 192]):

> To switch the radar between RWS (Range While Search) and TWS (Track While Scan) modes, press the TMS (Target Management Switch) RIGHT LONG (page 197).

**Holý LLM** (bez příručky):

> To switch the radar between RWS (Range While Search) and TWS (Track While Scan) modes in the F-16C Viper module in DCS, follow these steps:

1. **Ensure the Radar is Powered On**: Make sure the radar is operational. You can do this by checking the radar display on the Multi-Function Display (MFD).

2. **Select the Radar Mode**: 
   - Use the **Radar Mode Switch** on the throttle or the HOTAS (Hands On Throttle and Stick) controls. 
   - The switch is typically labeled as "RWS/TWS" or similar.

3. **Toggle Between Modes**: 
   - To switch to RWS, move the switch to the RWS position.
   - To switch to TWS, move the switch to the TWS position.

4. **Verify the Mode on the MFD**: After switching, check the radar display on the MFD to confirm that the mode has changed. You should see the corresponding indicators for RWS or TWS.

5. **Adjust Settings as Needed**: Depending on your mission requirements, you may want to adjust other radar settings such as range, elevation, and scan volume.

Remember that TWS mode allows you to track multiple targets simultaneously, while RWS is primarily for searching and detecting targets. Make sure to practice switching between these modes to become proficient in their use during missions.

**Hodnocení** (doplň ručně): citace sedí? ano sedí  RAG lepší? je lepší, dokonce má pravdu i nad očekáváno, obojí totiž jde  u 'mimo korpus' odmítl? netřeba

---

## [in corpus] How do I lock (bug) a target in BVR using the radar?

**Očekáváno** (strany [173, 182]): Slew the cursor over the contact and TMS forward (up) to bug/lock the target into a single-target-track; TMS aft to drop the lock.

**RAG** (našel strany [190, 451, 194, 540]):

> To lock (bug) a target in BVR using the radar, you can perform the following steps:

1. Use the Radar Cursor/Enable switch to move the Acquisition Cursor over the desired System Target.
2. Press TMS (Target Management Switch) UP to set the selected System Target into a Bugged Target (page 194).

Alternatively, you can bug the closest System Target to you by:

1. Pressing TMS (Target Management Switch) RIGHT SHORT.
2. The System Target closest to you will automatically be selected as the Bugged Target. Subsequent presses of TMS RIGHT SHORT will cycle through all displayed System Targets, making each the Bugged Target in turn (page 194). 

Once a Bugged Target is designated, the radar automatically transitions the scan to 3-bar, ±25 degrees centered on the bugged target to provide faster updates and reduce the chance of losing the track (page 190).

**Holý LLM** (bez příručky):

> To lock (bug) a target in Beyond Visual Range (BVR) using the radar in the F-16C Viper module in DCS, follow these steps:

1. **Set Radar to BVR Mode**: Ensure your radar is set to the appropriate BVR mode. You can do this by selecting the "TWS" (Track While Scan) mode or "RWS" (Range While Search) mode on the radar control panel.

2. **Scan for Targets**: Use the radar to search for targets. In TWS mode, the radar will automatically scan for multiple targets, while in RWS mode, you can manually adjust the radar elevation and azimuth to find targets.

3. **Identify Targets**: Once you detect a target, you can use the radar display to identify it. Look for the target symbol on your radar screen.

4. **Lock the Target**: To lock the target, you need to use the "TMS Up" (Targeting Management Switch Up) command. This will bug the target and allow you to track it. If you are in TWS mode, the radar will automatically track the target once it is locked.

5. **Check the HUD**: After locking the target, you should see the target information displayed on your HUD, including range, aspect, and other relevant data.

6. **Fire Weapons**: Once the target is locked and you have confirmed it is a valid target, you can proceed to fire your air-to-air missiles (AAMs) as necessary.

Remember to maintain situational awareness and be aware of your surroundings while engaging in BVR combat.

**Hodnocení** (doplň ručně): citace sedí? sedí  RAG lepší? oba odpověděli za mě ok  u 'mimo korpus' odmítl? netřeba

---

## [in corpus] How do I employ a JDAM (GBU-38) against a ground target?

**Očekáváno** (strany [314, 495]): Select the JDAM on the SMS, set the target steerpoint/coordinates, ensure the weapon is in range (HUD/launch cues), and release with the pickle button when within the release envelope.

**RAG** (našel strany [495, 496, 495, 509]):

> To employ a JDAM (GBU-38) against a ground target, follow these steps:

1. Verify that the FCR (Fire Control Radar) switch is ON (FWD); the FCR is used for target ranging.
2. If using a targeting pod laser to range the target, set the RIGHT HDPT switch to ON (FWD).
3. Set the Master Arm switch to ARM (UP).
4. Select Air-to-Ground Master Mode by pressing the A-G Button on the ICP (Integrated Control Panel). This configures the Fire Control Radar, Targeting Pod, and displays for air-to-ground attacks.
5. On the SMS (Stores Management Set) page, select GBU-38 JDAMS (GB38) by toggling weapons with the OSB (Option Select Button) adjacent to the Selected Weapon option.
6. Power on GBU-38s by pressing the OSB next to PWR. When the countdown starting from “A10” disappears and “PWR ON” and “RDY” indications are visible, the power-up sequence is complete.
7. Select the desired JDAM station by pressing the NWS / MSL STEP button on the stick for less than 0.5 seconds (SHORT) (pages 496-497). 

Make sure to perform target designation in either Pre-Planned or Visual Mode, verifying the target with appropriate sensors to avoid dropping ordnance at the wrong place (pages 495, 509).

**Holý LLM** (bez příručky):

> To employ a JDAM (GBU-38) against a ground target in the F-16C Viper module in DCS, follow these steps:

### Pre-Flight Preparation
1. **Load the JDAM:** Ensure that your aircraft is loaded with GBU-38s. You can do this in the mission editor or by using the aircraft's armament menu before takeoff.

### In-Flight Steps
2. **Set Up the Targeting System:**
   - Use the **TGP (Targeting Pod)** to identify and designate your target. You can use the TGP to visually confirm the target and get coordinates.
   - Alternatively, you can use the **HSD (Horizontal Situation Display)** to input coordinates manually if you have them.

3. **Select the JDAM:**
   - On the **MFD (Multi-Function Display)**, select the **Stores Page**.
   - Choose the GBU-38 from the list of available weapons.

4. **Set the JDAM to the Correct Mode:**
   - Ensure that the JDAM is set to **GPS** mode. This is typically the default mode for JDAMs.
   - You can also set the desired release parameters (such as release altitude and parameters) if needed.

5. **Designate the Target:**
   - If using the TGP, designate the target by pressing the **TMS Up** button (typically the Hat Switch) to create a target point (TP) in the system.
   - If you are using coordinates, input them into the JDAM's target data.

### Targeting and Release
6. **Check the Target Data:**
   - Verify that the target coordinates are correct on the JDAM page. You should see the target point and any relevant data.

7. **Set the Release Parameters:**
   - Adjust your altitude and speed to ensure you are within the effective release parameters for the JDAM. Generally, a release altitude of 15,000 feet or higher is recommended for optimal performance.

8. **Fly to the Release Point:**
   - Navigate to the target area and ensure you are on the correct heading and altitude for release.

9. **Release the JDAM:**
   - When you are in the correct position, press the weapon release button (typically the trigger) to release the JDAM.
   - Ensure you maintain a safe distance from the target to avoid any potential blast effects.

### Post-Release
10. **Monitor the Impact:**
    - Use the TGP to visually confirm the impact of the JDAM on the target.
    - Assess the damage and determine if additional strikes are needed.

### Additional Tips
- **Practice:** Familiarize yourself with the JDAM's capabilities and practice in a training environment to improve your accuracy.
- **Check for Updates:** Ensure your DCS module is updated, as features and functionalities may change with updates.

By following these steps, you should be able to effectively employ a JDAM against ground targets in the F-16C Viper module in DCS.

**Hodnocení** (doplň ručně): citace sedí? ano  RAG lepší? zde si nejsem jistý  u 'mimo korpus' odmítl? netřeba

---

## [in corpus] What is the correct procedure to fire an AIM-120 AMRAAM?

**Očekáváno** (strany [315, 318]): Select A-A mode and the AIM-120, lock the target, confirm it is within the launch zone (DLZ cues on HUD), and fire with the weapon-release/pickle.

**RAG** (našel strany [554, 553, 569, 318]):

> To fire an AIM-120 AMRAAM, follow these steps:

1. Select the desired missile using one of the following methods:
   - Press Dogfight Switch OUTBOARD (DGFT) to automatically select AIM-9 missiles, then select the AIM-120 missile from the SMS page.
   - Press Dogfight Switch INBOARD (MSL OVRD/Missile Override), then select the desired missile from the SMS page.
   - Select Air-to-Air Master Mode by pressing the A-A Button, then select the desired missile from the SMS page (page 554).

2. Acquire a radar lock on the target. The missile seeker will be slaved to the Fire Control Radar (FCR) in this mode (page 553).

3. Press the Target Management Switch (TMS) RIGHT SHORT to cycle to the next displayed system target if needed (page 569).

4. Depress the Weapon Release button (RALT+SPACE) to fire the missile (page 569).

5. Repeat steps 3 and 4 to engage further targets if necessary (page 569).

**Holý LLM** (bez příručky):

> To fire an AIM-120 AMRAAM (Advanced Medium-Range Air-to-Air Missile) in the DCS F-16C Viper module, follow these steps:

1. **Select the AIM-120**: Ensure that the AIM-120 is loaded on the aircraft. Use the UFC (Up Front Control) to select the appropriate weapon. You can do this by pressing the weapon select button on the throttle or using the DED (Data Entry Display) to select the AIM-120.

2. **Set the Master Arm**: Ensure that the Master Arm switch is set to "ARM." This is necessary to enable the firing of weapons.

3. **Select the Target**: Use the radar to locate and lock onto the target. You can do this by using the radar cursor to designate the target and pressing the "TMS Up" (Targeting Management Switch) to lock it.

4. **Check the Launch Parameters**: Ensure that the target is within the effective range of the AIM-120 and that the launch parameters are met (such as aspect angle, altitude, and range). The HUD will provide indications if the target is within range and if the missile can be launched.

5. **Launch the Missile**: Once the target is locked and the launch parameters are satisfied, press the weapon release button (usually mapped to a button on your joystick or HOTAS). The AIM-120 will be launched.

6. **Monitor the Missile**: After launch, you can monitor the missile's flight and track the target using the radar. The AIM-120 will autonomously guide itself to the target after launch.

7. **Post-Launch Actions**: After firing, you may want to re-engage or maneuver for another target, depending on the tactical situation.

Remember to practice these steps in a training environment to become familiar with the controls and procedures.

**Hodnocení** (doplň ručně): citace sedí? našel lepší  RAG lepší? oba ok?  u 'mimo korpus' odmítl? netřeba

---

## [in corpus] How do I set up and employ the AGM-88 HARM?

**Očekáváno** (strany [436]): Select the HARM on the SMS, choose the employment mode (e.g., POS/HAS), have it detect/handoff the radar emitter threat, then release within parameters.

**RAG** (našel strany [445, 453, 437, 466]):

> To set up and employ the AGM-88 HARM, follow these steps:

1. Press the A-G Master Mode Button.
2. Set the Master Arm switch to ARM (UP).
3. On the SMS (Stores Management Set) page, press the OSB (Option Select Button) next to the current Missile Type to toggle to the AG88 (AGM-88C HARM) missile. The number preceding AG88 indicates the number of missiles of this type equipped.
4. Select the desired missile station by pressing the NWS / MSL STEP button on the stick for less than 0.5 seconds (SHORT).
5. Press the OSB next to PWR OFF to start the power-up process of the HARM. A BIT (Built-In Test) will be initiated (pages 445, 453, 466).

**Holý LLM** (bez příručky):

> To set up and employ the AGM-88 HARM (High-speed Anti-Radiation Missile) on the F-16C Viper in DCS, follow these steps:

### 1. **Loadout Configuration**
   - **Select the AGM-88 HARM**: In the mission editor or during the pre-flight setup, ensure that you have selected the AGM-88 HARM as part of your weapon loadout. You can typically load 2 or 4 HARMs on the aircraft's wing pylons.

### 2. **Power Up and Systems Check**
   - **Start the Aircraft**: Power up the F-16C and ensure all systems are operational.
   - **Check the HARM System**: After starting the aircraft, check the HARM system by selecting the appropriate weapon control panel.

### 3. **Select the HARM Mode**
   - **Switch to the HARM Mode**: On the DED (Data Entry Display), navigate to the HARM page. You can do this by pressing the appropriate button on the UFC (Up Front Controller) or using the MFD (Multi-Function Display).
   - **Select the Desired Mode**: The HARM can be set to different modes, such as:
     - **SCS (Self-Contained System)**: For general use.
     - **SLEW**: To manually target a radar source.
     - **AUTO**: For automatic targeting of detected radar emissions.

### 4. **Targeting**
   - **Use the RWR (Radar Warning Receiver)**: The RWR will help you identify enemy radar sources. Look for the radar signals that are detected.
   - **Designate the Target**: If in SLEW mode, you can use the TDC (Target Designation Controller) to point the targeting cursor at the radar source you want to engage.

### 5. **Launch the HARM**
   - **Check the Launch Parameters**: Ensure you are within range and that the target is locked (if applicable).
   - **Fire the Missile**: Once you have a target and are ready to engage, press the weapon release button to launch the AGM-88 HARM.

### 6. **Post-Launch**
   - **Monitor the Missile**: After launch, you can monitor the missile's flight path and impact through the HUD or MFD.
   - **Assess Damage**: After the missile has impacted, assess the damage to the target and adjust your tactics as necessary.

### 7. **Tactical Considerations**
   - **Avoiding Enemy Air Defenses**: When employing HARMs, be aware of enemy air defenses and plan your ingress and egress routes accordingly.
   - **Use of ECM**: Consider using electronic countermeasures (ECM) to reduce the effectiveness of enemy radar while you engage with HARMs.

### Additional Tips
- **Practice**: Familiarize yourself with the HARM's capabilities and limitations through practice missions.
- **Consult the Manual**: Refer to the DCS F-16C manual for detailed information on the HARM and its systems.

By following these steps, you should be able to effectively set up and employ the AGM-88 HARM on the F-16C Viper in DCS. Happy flying!

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] How do I employ the AGM-65 Maverick?

**Očekáváno** (strany [394]): Select the Maverick, uncage/slave the seeker to the target (via TGP or boresight), get a lock on the target, then fire with the pickle button.

**RAG** (našel strany [415, 395, 416, 405]):

> To employ the AGM-65 Maverick, follow these steps:

1. Press the A-G Master Mode Button.
2. Set the Master Arm switch to ARM (UP).
3. On the SMS (Stores Management Set) page, press the OSB (Option Select Button) next to the current Missile Type to toggle to the AG65 (AGM-65 Maverick) missile.
4. Select the desired missile station by pressing the NWS / MSL STEP button on the stick for less than 0.5 seconds (SHORT).
5. Toggle the OSB next to Maverick Mode to select the desired mode (BORE or PRE).
6. If using LAU-88 missile racks, select the desired Ripple Quantity using the OSB next to RP.
7. Power up the Maverick and start seeker cooldown (MANUAL cooldown method):
   a. From the SMS page, press the OSB next to PWR OFF to start the power-up process of the Maverick.
   b. Once PWR ON is set, cooldown will take about 3 minutes.
8. If using the AGM-65G variant with a targeting pod, ensure the FCR (Fire Control Radar) switch is ON, set the RIGHT HDPT switch to ON, and set the Laser Switch to ARMED before proceeding with the missile launch (page 405).

Finally, depress the Weapon Release (RALT+SPACE) button to fire the missile (page 415).

**Holý LLM** (bez příručky):

> To employ the AGM-65 Maverick on the F-16C Viper in DCS, follow these steps:

### 1. **Loadout Configuration:**
   - Ensure that your aircraft is loaded with AGM-65 Mavericks. You can do this in the mission editor or by using the ground crew in the game.

### 2. **Select the Maverick:**
   - Once in the cockpit, access the **Stores Management System (SMS)** by pressing the appropriate button (usually the SMS button on the UFC).
   - Select the AGM-65 by cycling through the available stores until you highlight the Maverick.

### 3. **Set the Targeting System:**
   - Switch to the **Maverick display** by selecting the appropriate display on the Multi-Function Display (MFD).
   - Use the **TGP (Targeting Pod)** or the Maverick's own seeker head to designate your target. If using the TGP, ensure it is powered on and in the correct mode.

### 4. **Designate the Target:**
   - If using the TGP, designate the target by using the TGP's targeting functions (usually by pressing the TMS button).
   - If using the Maverick's seeker, switch to the Maverick mode and use the **TDC (Target Designation Cursor)** to lock onto the target.

### 5. **Check the Lock:**
   - Ensure that the Maverick has a solid lock on the target. The display will indicate a successful lock.

### 6. **Launch the Maverick:**
   - Once locked, you can launch the missile by pressing the weapon release button (usually the trigger on the control stick).
   - Monitor the missile's flight and impact on the target.

### 7. **Post-Launch:**
   - After launch, you can switch back to other systems or prepare for another engagement if you have additional Mavericks or other ordnance.

### Additional Tips:
- **Tactical Considerations:** The AGM-65 is effective against armored vehicles and other ground targets. Be aware of your launch parameters and the range of the missile.
- **Use of TGP:** The TGP can provide better target identification and tracking, especially in adverse weather conditions or low visibility.
- **Practice:** Familiarize yourself with the Maverick's capabilities and limitations through practice missions to improve your proficiency.

By following these steps, you should be able to effectively employ the AGM-65 Maverick in DCS with the F-16C Viper.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] How do I perform an ILS landing in the F-16C?

**Očekáváno** (strany [675, 771]): Tune the ILS frequency, set the instrument mode, follow the localizer and glideslope cues on the HUD/ADI down to the runway.

**RAG** (našel strany [769, 774, 775, 728]):

> To perform an ILS landing in the F-16C, follow these steps:

1. **ILS Frequency and Runway Information**: Tune to the ILS frequency of 110.30 for Batumi airfield’s runway 13. The runway heading is 120 Magnetic Heading / 126 True Heading (page 769).

2. **Approach**: As you approach the runway, when flying over the “overrun” (the portion of the runway before the primary surface starts), shift the Flight Path Marker forward to a point 300-500 ft down the runway (page 774).

3. **Flare and Touchdown**: Gently pull back on the stick to flare and reduce the descent rate. Do not level off! Pull the throttle back to IDLE and touchdown with a maximum Angle of Attack (AOA) of 13 degrees (green circle). Be cautious, as more than 15 degrees AOA during the landing roll-out may cause the speedbrakes or engine nozzle to hit the runway (page 774).

4. **Aerodynamic Braking**: Maintain a 13-degree nose-up attitude for two-point aerodynamic braking until your airspeed reduces to approximately 100 knots. This is crucial since the F-16’s brakes are not very effective (page 775).

5. **Lower Nosewheel**: Reduce back stick pressure and lower the nosewheel to the runway (page 775).

6. **Speedbrakes and Braking**: Open the speedbrakes fully and maintain full aft stick for maximum braking effectiveness. Apply moderate to heavy braking to slow the aircraft (page 775).

7. **Taxi Off**: Engage nosewheel steering when below 30 knots and taxi off the runway (page 775). 

These steps will guide you through the ILS landing process in the F-16C.

**Holý LLM** (bez příručky):

> Performing an ILS (Instrument Landing System) landing in the F-16C Viper involves several steps. Here’s a general guide to help you through the process:

### Pre-Flight Preparation
1. **Set Up the Mission**: Ensure you have an ILS approach available for your destination airport. Check the approach charts for the correct frequency and course.

2. **Configure the HUD**: Make sure your HUD is set to display the necessary information for the approach. You may want to have the ILS frequency tuned and the course set.

### In-Flight Procedure
1. **Tune the ILS Frequency**: 
   - Access the UFC (Up Front Controller) and input the ILS frequency for your destination airport. 
   - Confirm that the frequency is active in the HSI (Horizontal Situation Indicator).

2. **Set the Course**: 
   - Set the course on the HSI to match the ILS approach course.

3. **Approach Configuration**: 
   - As you approach the airport, descend to the appropriate altitude for the ILS approach. 
   - Ensure your aircraft is configured for landing (gear down, flaps set, etc.).

4. **Intercept the Localizer**: 
   - Fly towards the ILS localizer. The HSI will show you whether you are to the left or right of the localizer. 
   - Adjust your heading to intercept the localizer beam.

5. **Capture the Glide Slope**: 
   - Once you are established on the localizer, descend to capture the glide slope. 
   - The glide slope indicator on the HSI will show whether you are above or below the glide slope.

### Final Approach
1. **Maintain Control**: 
   - Keep the aircraft aligned with the localizer and on the glide slope. Use small adjustments to your heading and altitude as needed.

2. **Monitor Airspeed**: 
   - Maintain the appropriate approach speed for landing. 

3. **Visual Reference**: 
   - As you get closer to the runway, switch to visual references if conditions allow. 

### Landing
1. **Flare and Touchdown**: 
   - As you reach the runway threshold, perform a flare to reduce your descent rate and touchdown gently.

2. **Roll Out**: 
   - After touchdown, apply brakes and steer the aircraft to exit the runway safely.

### Post-Landing
1. **Taxi to Parking**: 
   - Follow taxiway instructions to reach your parking spot.

### Additional Tips
- **Practice**: ILS landings can be tricky, so practice in different weather conditions to improve your skills.
- **Use the Checklist**: Always refer to the aircraft's checklist for specific procedures related to ILS approaches and landings.

By following these steps, you should be able to successfully perform an ILS landing in the F-16C Viper. Happy flying!

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [OUT of corpus] How do I start the engines on the F/A-18C Hornet?

**Očekáváno** (strany []): Different aircraft not covered by this guide. The assistant should state the answer is not in the F-16 guide and not make it up.

**RAG** (našel strany [85, 90, 91, 118]):

> I do not have information on starting the engines of the F/A-18C Hornet. The excerpts provided only cover the start-up procedure for the F-16C Viper.

**Holý LLM** (bez příručky):

> To start the engines on the F/A-18C Hornet in DCS, follow these steps:

1. **Power On**: Ensure the battery is on. You can do this by flipping the battery switch to the ON position.

2. **Fuel System**: Make sure the fuel system is set correctly. Check that the fuel pumps are on. You can do this by turning on the fuel boost pumps.

3. **Engine Start Switch**: Locate the engine start switch on the right side of the cockpit. Set the switch to the "START" position for the engine you want to start (either left or right).

4. **Monitor RPM**: Watch the RPM gauge for the engine you are starting. Once the RPM reaches around 20%, you can move the engine start switch to the "RUN" position.

5. **Repeat for Second Engine**: If you are starting the second engine, repeat the process for the other engine.

6. **Check Engine Instruments**: After both engines are started, check the engine instruments to ensure they are operating within normal parameters.

7. **After Start Checks**: Perform any necessary after-start checks, such as verifying that the engine instruments are in the green and that all systems are functioning properly.

Remember to follow any specific procedures or checklists you may have for your mission or flight profile. Enjoy your flight in the Hornet!

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [OUT of corpus] What is the real-world combat radius of the F-16 in kilometers?

**Očekáváno** (strany []): Real-world performance figure, not a DCS procedure from this guide. The assistant should say it is not in the guide.

**RAG** (našel strany [2, 174, 391, 8]):

> The excerpts provided do not contain information about the real-world combat radius of the F-16 in kilometers.

**Holý LLM** (bez příručky):

> The real-world combat radius of the F-16C Viper varies depending on the specific configuration, mission profile, and loadout. However, a general estimate for the combat radius of the F-16C is approximately 550 to 600 kilometers (about 340 to 370 miles) when carrying a typical loadout and flying at a moderate altitude. This range can be affected by factors such as fuel load, weapons, and mission type.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [OUT of corpus] How do I activate the IRST (infrared search and track) sensor on the F-16C?

**Očekáváno** (strany []): The DCS F-16C does not have an IRST; the guide does not cover it. The assistant should say the answer is not in the guide rather than inventing a procedure.

**RAG** (našel strany [273, 763, 192, 198]):

> The guide excerpts do not provide information on how to activate the IRST (infrared search and track) sensor on the F-16C.

**Holý LLM** (bez příručky):

> In the F-16C Viper module for DCS, the F-16C does not have an IRST (Infrared Search and Track) sensor as part of its standard avionics suite. The F-16C primarily relies on its radar and other sensors for target acquisition and tracking.

If you are looking for infrared targeting capabilities, you would typically use the AN/AAQ-28 LITENING targeting pod or similar systems, which can be used for targeting and reconnaissance. To use such a pod, you would need to ensure it is loaded on the aircraft and then follow these general steps:

1. **Select the Targeting Pod**: Use the UFC (Up Front Control) to select the targeting pod.
2. **Power On the Pod**: Ensure the targeting pod is powered on and operational.
3. **Switch to the Pod's Video Feed**: Use the MFD (Multi-Function Display) to switch to the targeting pod's video feed.
4. **Use the TDC (Target Designation Controller)**: Control the pod's sensors and designate targets as needed.

If you are looking for a specific feature or capability, please clarify, and I can provide more detailed instructions!

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

