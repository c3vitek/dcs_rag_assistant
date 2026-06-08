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
6. When the JFS is operational, a clutch will engage, driving the engine through the accessory drive gearbox (page 91).
7. When engine RPM reaches between 20% and 25%, move the throttle from the OFF position to the IDLE position (RSHIFT+HOME). Be cautious not to move the throttle too early to avoid a hot start or hung start (page 91).
8. The engine should light-off within 10 seconds, and engine RPM and FTIT (Fan Turbine Inlet Temperature) should increase (page 91). 

Follow these steps carefully to successfully start the engine using the JFS.

**Holý LLM** (bez příručky):

> To start the engine on the F-16C using the Jet Fuel Starter (JFS), follow these steps:

1. **Pre-Start Checks**:
   - Ensure that the aircraft is in a safe environment for engine start.
   - Check that the battery is on and the fuel system is configured correctly.

2. **Set the Throttle**:
   - Move the throttle to the **IDLE** position (approximately 1/4 forward).

3. **JFS Start Switch**:
   - Locate the **JFS Start Switch** on the throttle quadrant.
   - Press the **JFS Start Switch** to the **START** position. This will initiate the JFS and begin the engine start sequence.

4. **Monitor Engine Parameters**:
   - Watch the **RPM** gauge on the engine instruments. The RPM should start to rise.
   - Monitor the **EGT (Exhaust Gas Temperature)**. Ensure it stays within acceptable limits during the start.

5. **Fuel Flow**:
   - Once the RPM reaches around 20% to 25%, the fuel flow should automatically start. You should see the fuel flow indicator rise.

6. **Engine Start**:
   - Continue to monitor the RPM. Once it reaches approximately 50%, the engine is considered to be starting successfully.
   - If the engine does not start within a certain time (usually around 30 seconds), you may need to abort the start and try again.

7. **JFS Start Switch**:
   - Once the engine is stable and running (RPM is above 60% and EGT is within limits), release the **JFS Start Switch** back to the **NORM** position.

8. **Post-Start Checks**:
   - Check all engine parameters to ensure they are within normal operating limits.
   - Ensure that the engine is stable and that all systems are functioning correctly.

9. **Throttle Position**:
   - After the engine is stable, you can move the throttle to the desired position for taxiing or takeoff.

Remember to follow any specific procedures outlined in the F-16C manual or your training materials, as there may be variations based on the specific aircraft configuration or mission requirements.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] How do I align the INS before flight?

**Očekáváno** (strany [96, 97]): Set the INS knob to ALIGN NORM and wait for a full alignment (typically ~8 minutes); the DED shows the alignment status/quality before switching to NAV.

**RAG** (našel strany [97, 96, 99, 98]):

> To align the INS (Inertial Navigation System) before flight, follow these steps:

1. **Set the INS Selector Switch**: Choose either a Normal alignment or a Stored Heading alignment. For Normal alignment, set the switch to ALIGN NORM, which takes approximately 8 minutes. For Stored Heading alignment, set it to ALIGN STOR HDG, which takes about 90 seconds (page 96).

2. **Enter Aircraft Coordinates**: If performing a Normal alignment, enter and confirm the aircraft coordinates on the INS DED page within two minutes after starting the alignment. Check the coordinates via the F10 map and ensure they are in Degrees, Minute, Decimal-Minutes format (page 97).

3. **Confirm Latitude and Longitude**: Confirm that the latitude coordinates match the aircraft's coordinates and press the “ENTR” button on the ICP to enter/confirm the latitude. Then, select the longitude coordinates (page 97).

4. **Monitor Alignment Status**: Watch for the INS Alignment Status to reach “10 RDY”, which indicates that the alignment is complete (page 98).

5. **Set to NAV**: Once the alignment is complete, set the INS Selector Switch to NAV (Navigation) (page 99).

Make sure to follow these steps carefully to ensure proper INS alignment before flight.

**Holý LLM** (bez příručky):

> To align the Inertial Navigation System (INS) in the F-16C Viper module in DCS (Digital Combat Simulator), follow these steps:

1. **Power Up the Aircraft**: Ensure that the aircraft is powered on. You can do this by turning on the battery and the external power if available.

2. **Set the INS Mode**: On the DED (Data Entry Display), select the INS page. You can do this by pressing the appropriate button on the UFC (Up Front Controller) or using the MFD (Multi-Function Display) controls.

3. **Select the Alignment Mode**: 
   - On the DED, you will see options for different alignment modes. Choose the "NAV" mode for normal navigation alignment.
   - If you are on the ground, you may also see options for "Ground" alignment.

4. **Enter the Position**: 
   - You will need to enter your current position (latitude and longitude) into the INS. This can be done using the UFC. 
   - Use the UFC to input your coordinates. Make sure to enter them accurately.

5. **Start the Alignment**: 
   - Once the position is entered, initiate the alignment process. This is usually done by pressing the "ALIGN" button on the DED or UFC.
   - The alignment process will take a few minutes (typically around 5-10 minutes). During this time, the system will calibrate itself based on the entered position.

6. **Monitor the Alignment Status**: 
   - Keep an eye on the DED for the alignment status. It will indicate when the alignment is complete. You should see a message indicating that the INS is ready for use.

7. **Check the Navigation System**: 
   - Once aligned, verify that the navigation system is functioning correctly. You can do this by checking the navigation display and ensuring that your position is accurately represented.

8. **Final Checks**: 
   - Before takeoff, ensure that all systems are operational and that you have set your waypoints and other navigation settings as needed.

Once the INS is aligned and ready, you can proceed with your flight preparations. Remember that proper alignment is crucial for accurate navigation during your mission.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] What is the maximum G limit of the F-16C?

**Očekáváno** (strany [154]): Around 9 G; the FLCS limits the airframe, with lower limits at heavy gross weight / with stores.

**RAG** (našel strany [7, 666, 5, 6]):

> The maximum G limit of the F-16C is +9 G in the CAT I configuration (Air-to-Air) until 15 degrees AoA (Angle of Attack) is reached. Above 15 degrees AoA, the maximum G is a function of AoA and airspeed, with a maximum of +7.3 G at 20 degrees AoA and +1 G at 25 degrees AoA (page 666). In the CAT III configuration (Air-to-Ground), the FCS limits aircraft acceleration from -3 G to +9 G until 15 degrees AoA is reached, and the maximum AoA is limited to 15.5 - 15.8 degrees (page 666).

**Holý LLM** (bez příručky):

> The maximum G limit of the F-16C Viper is typically around +9 Gs in a clean configuration. However, this limit can vary based on factors such as weight, fuel load, and specific aircraft configurations. It's important to consult the specific aircraft's flight manual for precise limits under different conditions.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] At what speed should I take off / rotate?

**Očekáváno** (strany [123]): Takeoff at approx. 173 kts; begin rotation roughly 10 kts below takeoff speed (around 160-163 kts).

**RAG** (našel strany [123, 744, 746, 416]):

> Your takeoff speed is approximately 173 knots for a takeoff weight of 34,000 lbs. You should gently pull back on the stick and establish a takeoff attitude (8-12 degrees of pitch) at approximately 10 knots below the takeoff speed, which would be around 163 knots in this case (page 123).

**Holý LLM** (bez příručky):

> For the F-16C Viper, the recommended rotation speed (Vr) for takeoff typically ranges between 130 to 150 knots, depending on factors such as aircraft weight, configuration, and environmental conditions. 

As a general guideline:

- **Light Load (e.g., fuel and ordnance)**: Around 130 knots
- **Medium Load**: Approximately 140 knots
- **Heavy Load**: Closer to 150 knots

Always refer to the specific aircraft's flight manual or performance charts for the most accurate takeoff speeds based on your current weight and configuration. Additionally, ensure you are aware of the runway length and conditions, as these can also affect your takeoff performance.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] What does the Master Caution light mean and how do I reset it?

**Očekáváno** (strany [35]): It signals a caution; check the caution panel for the specific warning, then press the Master Caution button to reset the light.

**RAG** (našel strany [597, 112, 35, 22]):

> The Master Caution light indicates that there is a fault that requires attention. To reset it, you need to press the Master Caution Light (Push to Reset) button (page 35).

**Holý LLM** (bez příručky):

> In the F-16C Viper, the Master Caution light indicates that there is a system warning or caution that requires your attention. This light will illuminate when there are any alerts from various systems, such as engine, fuel, electrical, or other critical systems.

To reset the Master Caution light, you can follow these steps:

1. **Identify the Warning**: First, check the warning lights and the caution messages on the Multi-Function Display (MFD) or the caution panel to determine the specific issue that triggered the Master Caution.

2. **Address the Issue**: Resolve the underlying issue that caused the Master Caution to illuminate. This may involve adjusting settings, troubleshooting systems, or performing necessary actions based on the warning.

3. **Reset the Master Caution**: Once the issue is addressed, you can reset the Master Caution light by pressing the Master Caution reset button, which is typically located on the front of the throttle or on the caution panel.

After pressing the reset button, the Master Caution light should turn off if all issues have been resolved. Always ensure that you have addressed the underlying problem before resetting the light to avoid missing critical alerts.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] How do I switch the radar between RWS and TWS modes?

**Očekáváno** (strany [173, 176]): Use the OSB next to the radar mode label on the FCR page to cycle the air-to-air mode between RWS and TWS.

**RAG** (našel strany [197, 186, 556, 192]):

> To switch the radar between RWS (Range While Search) and TWS (Track While Scan) modes, press the TMS (Target Management Switch) RIGHT LONG (page 197).

**Holý LLM** (bez příručky):

> To switch the radar between RWS (Range While Search) and TWS (Track While Scan) modes in the F-16C Viper module in DCS, follow these steps:

1. **Ensure the Radar is Powered On**: Make sure the radar is operational. You can do this by checking the radar display on the Multi-Function Display (MFD).

2. **Select the Radar Mode**: 
   - Use the **Radar Mode Switch** on the throttle or the control panel. 
   - You can typically find this switch labeled as "RWS" and "TWS" on the radar control panel.

3. **Toggle Between Modes**: 
   - To switch to RWS, simply select the RWS option.
   - To switch to TWS, select the TWS option.

4. **Confirm the Mode Change**: Look at the radar display on the MFD to confirm that the mode has changed. The display should indicate whether you are in RWS or TWS mode.

5. **Adjust Settings as Necessary**: Depending on your mission requirements, you may want to adjust other radar settings such as range and elevation.

Make sure to practice switching between these modes in a training environment to become familiar with the radar system's capabilities and limitations.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

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

1. **Set the Radar Mode**: Ensure your radar is set to the appropriate mode for BVR engagement. Typically, you would use the **TWS (Track While Scan)** mode for BVR engagements. You can switch to TWS by pressing the **TWS button** on the radar control panel.

2. **Scan for Targets**: Use the radar to scan for targets. You can adjust the radar's range and elevation settings to optimize your search. The radar display will show potential targets as blips.

3. **Select a Target**: Once you have detected a target, use the **Target Designation Switch** (usually the **TMS Up** button) to designate the target. This will highlight the target on your radar display.

4. **Bug the Target**: After designating the target, press the **TMS Right** button to "bug" the target. This action will lock the target and allow you to track it. The radar will now focus on this target, and you will receive information about its range and aspect.

5. **Check Target Information**: Once the target is locked, you can check the target information on your HUD and radar display. This will include range, altitude, and aspect, which are crucial for BVR engagements.

6. **Prepare for Engagement**: With the target locked, you can prepare to engage using your air-to-air missiles. Ensure you have the correct weapon selected and that you are within range for a successful shot.

Remember to maintain situational awareness and be aware of your own aircraft's position and any potential threats while engaging in BVR combat.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

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

Additionally, ensure to perform target designation in either Pre-Planned or Visual Mode, verifying the target with appropriate sensors to avoid dropping ordnance at the wrong place (pages 495, 509).

**Holý LLM** (bez příručky):

> To employ a JDAM (GBU-38) against a ground target in the F-16C Viper module in DCS, follow these steps:

### Pre-Flight Preparation
1. **Load the JDAM:** Ensure that your aircraft is loaded with GBU-38s. You can do this in the mission editor or by using the aircraft's armament menu in-flight.

### In-Flight Steps
2. **Set Up the Targeting System:**
   - Use the **TGP (Targeting Pod)** to identify and designate your target. You can do this by:
     - Switching to the TGP using the appropriate HOTAS commands.
     - Slewing the TGP to the target and locking it (usually by pressing the TMS Up button).
   
3. **Select the JDAM:**
   - On the **MFD (Multi-Function Display)**, select the JDAM weapon by navigating to the **Stores Page** and selecting the GBU-38.

4. **Set the JDAM to the Desired Mode:**
   - Ensure the JDAM is set to the correct mode (usually **GPS** mode for JDAMs). This is typically the default setting.

5. **Designate the Target:**
   - If you have the target locked with the TGP, you can designate it as the target for the JDAM. This is done by pressing the TMS Right button to send the target coordinates to the JDAM.

### Release Procedure
6. **Check the Release Parameters:**
   - Ensure that you are within the effective range for the JDAM and that your altitude and speed are appropriate for release. The JDAM can be released from high altitudes and at various speeds, but optimal conditions will yield better accuracy.

7. **Release the JDAM:**
   - Once you are in a suitable position and have confirmed the target, press the weapon release button (usually the trigger on the HOTAS) to release the JDAM.

### Post-Release
8. **Monitor the Impact:**
   - After releasing the JDAM, you can switch back to the TGP to visually assess the impact on the target. This can help you confirm the effectiveness of the strike.

### Additional Tips
- **Use the Data Link:** If you have a data link with other aircraft or ground units, you can receive target information that can assist in targeting.
- **Practice:** Familiarize yourself with the JDAM's capabilities and limitations through practice missions to improve your accuracy and effectiveness.

By following these steps, you should be able to effectively employ a JDAM against ground targets in the F-16C Viper module in DCS.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] What is the correct procedure to fire an AIM-120 AMRAAM?

**Očekáváno** (strany [315, 318]): Select A-A mode and the AIM-120, lock the target, confirm it is within the launch zone (DLZ cues on HUD), and fire with the weapon-release/pickle.

**RAG** (našel strany [554, 553, 569, 318]):

> To fire an AIM-120 AMRAAM, follow these steps:

1. Select the AIM-120 missile using one of the following methods:
   - Press the Dogfight Switch INBOARD (MSL OVRD/Missile Override) and then select the AIM-120 from the SMS page.
   - Select Air-to-Air Master Mode by pressing the A-A Button, and then select the AIM-120 from the SMS page (page 554).

2. Acquire a radar lock on the target. The missile seeker will be slaved to the Fire Control Radar (FCR) in this mode (page 553).

3. To engage other targets, press the Target Management Switch (TMS) RIGHT SHORT to cycle to the next displayed system target (page 569).

4. Depress the Weapon Release button (RALT+SPACE) to fire the missile (page 569).

5. Repeat the steps to engage further targets if necessary (page 569).

**Holý LLM** (bez příručky):

> To fire an AIM-120 AMRAAM (Advanced Medium-Range Air-to-Air Missile) in the DCS F-16C Viper module, follow these steps:

1. **Preparation:**
   - Ensure that the AIM-120 is loaded on the aircraft.
   - Set the appropriate weapon mode on the aircraft's systems.

2. **Select the AIM-120:**
   - Use the UFC (Up Front Control) or the DED (Data Entry Display) to select the AIM-120 as your active weapon.
   - Ensure that the missile is selected in the stores management system.

3. **Target Acquisition:**
   - Use the radar to search for and lock onto a target. You can use the TWS (Track While Scan) or STT (Single Target Track) modes depending on the situation.
   - Ensure that the target is within the effective range of the AIM-120 (typically 20-100 nautical miles, depending on conditions).

4. **Launch Authorization:**
   - Once the target is locked, check the missile status on the HUD (Head-Up Display) or MFD (Multi-Function Display) to ensure it is ready to fire.
   - The AIM-120 will typically show a launch cue on the HUD when conditions are met.

5. **Firing the Missile:**
   - Press the weapon release button (usually the trigger on the control stick) to launch the AIM-120.
   - Monitor the missile's flight path and the target's status.

6. **Post-Launch:**
   - After firing, you can continue to track the target or engage additional targets as necessary.
   - Be aware of the missile's flight time and the target's potential maneuvers.

7. **Re-engagement:**
   - If the target is still a threat after the missile launch, prepare to engage with additional weapons or tactics as needed.

Always refer to the specific DCS F-16C Viper manual or training resources for detailed procedures and any updates to the systems.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

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
   - **Select the AGM-88 HARM**: In the mission editor or during the pre-flight setup, ensure that you select the AGM-88 HARM as part of your weapon loadout. You can typically load them on the appropriate stations (usually stations 5 and 6).

### 2. **Aircraft Systems Setup**
   - **Power On**: Start the aircraft and ensure all systems are powered up.
   - **Select the Right Mode**: Set the HARM to the appropriate mode. The HARM can operate in different modes, such as:
     - **SCS (Self-Contained System)**: For general use.
     - **AGM-88 Mode**: This is typically selected via the DED (Data Entry Display) or the HARM control panel.

### 3. **Targeting**
   - **Radar and Target Acquisition**: Use your radar to locate enemy radar emitters. The HARM is designed to home in on radar emissions, so you need to identify targets that are actively emitting.
   - **HARM Targeting**: You can use the HARM's targeting system to find and lock onto enemy radar sources. This is done through the HARM control panel or the DED.

### 4. **HARM Control Panel**
   - **Select HARM Mode**: On the HARM control panel, select the desired mode (e.g., "SCS" or "AGM-88").
   - **Set the Desired Parameters**: Adjust parameters such as launch range and target type if necessary.

### 5. **Launch the HARM**
   - **Designate Target**: Once you have a target locked, you can designate it for launch.
   - **Launch**: Press the weapon release button to launch the AGM-88 HARM. Ensure you are within the effective range for the missile to engage the target.

### 6. **Post-Launch**
   - **Monitor the Missile**: After launch, monitor the missile's flight path and ensure it is tracking the target.
   - **Situational Awareness**: Maintain situational awareness and be prepared to evade any incoming threats, as launching HARMs can often reveal your position to enemy air defenses.

### 7. **Engagement and Follow-Up**
   - **Assess Damage**: After the missile has impacted, assess the damage to the target. If necessary, you may need to engage additional targets or provide further support.

### Additional Tips:
- **Practice**: Familiarize yourself with the HARM's capabilities and limitations through practice missions.
- **Use of Tactics**: Employ tactics such as flying at low altitude to avoid enemy radar detection and using terrain for cover.
- **Coordination with Other Assets**: Coordinate with other aircraft or ground forces to maximize the effectiveness of your strike.

By following these steps, you should be able to effectively set up and employ the AGM-88 HARM on the F-16C Viper in DCS.

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
8. If using the AGM-65G variant with a targeting pod, ensure the FCR (Fire Control Radar) switch is ON, set the RIGHT HDPT switch to ON, and set the Laser Switch to ARMED before proceeding with the launch (pages 395, 405, 416).

Finally, depress the Weapon Release (RALT+SPACE) button to fire the missile (page 415).

**Holý LLM** (bez příručky):

> To employ the AGM-65 Maverick missile on the F-16C Viper in DCS, follow these steps:

### 1. **Load the Maverick:**
   - Ensure that your aircraft is loaded with AGM-65 Mavericks. You can do this in the mission editor or by using the appropriate ground crew commands before takeoff.

### 2. **Select the Maverick:**
   - After takeoff, switch to the appropriate weapon mode. Use the **DMS (Data Management Switch)** on the throttle to select the Maverick. You can do this by pressing the DMS right to cycle through the weapon stations until you select the Maverick.

### 3. **Set the Targeting System:**
   - Use the **TGP (Targeting Pod)** or the **Maverick's own seeker** to designate your target. If using the TGP:
     - Designate the target using the TGP and ensure it is in the field of view.
     - Press the **TMS (Target Management Switch)** up to designate the target.
   - If using the Maverick's seeker:
     - Switch to the Maverick's seeker view by pressing the appropriate button (usually the **MAV** button on the UFC or the HOTAS).

### 4. **Lock the Target:**
   - Once the target is in view, press the **TMS up** to lock the target. The Maverick should now be tracking the target.

### 5. **Check the Launch Parameters:**
   - Ensure you are within the effective range of the Maverick (typically 8-12 miles, depending on the variant and conditions).
   - Check your altitude and speed; the missile performs best when launched from a stable platform.

### 6. **Launch the Missile:**
   - Once the target is locked and you are in a good position, press the weapon release button (usually the **trigger** on the HOTAS) to launch the missile.

### 7. **Monitor the Impact:**
   - After launch, you can continue to track the missile's flight using the TGP or the Maverick's seeker. Be prepared to adjust your flight path if necessary to avoid enemy defenses.

### 8. **Post-Launch:**
   - After firing, you can switch back to other weapons or continue to engage other targets as needed.

### Additional Tips:
- **Practice:** Familiarize yourself with the Maverick's capabilities and limitations in a training mission.
- **Situational Awareness:** Always maintain situational awareness of enemy threats, especially when engaging ground targets.
- **Use of TGP:** The TGP can greatly enhance your targeting capability, allowing for better identification and engagement of targets.

By following these steps, you should be able to effectively employ the AGM-65 Maverick in DCS with the F-16C Viper. Happy flying!

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [in corpus] How do I perform an ILS landing in the F-16C?

**Očekáváno** (strany [675, 771]): Tune the ILS frequency, set the instrument mode, follow the localizer and glideslope cues on the HUD/ADI down to the runway.

**RAG** (našel strany [769, 774, 775, 728]):

> To perform an ILS landing in the F-16C, follow these steps:

1. **ILS Frequency and Runway Information**:
   - Set the ILS frequency to 110.30.
   - The runway heading is 120 Magnetic Heading / 126 True Heading (page 769).

2. **Approach**:
   - When flying over the “overrun” (portion of the runway before the primary surface starts), shift the Flight Path Marker forward to a point 300-500 ft down the runway (page 774).

3. **Flare and Touchdown**:
   - Gently pull back on the stick to flare and reduce the descent rate. DO NOT level off (page 774).
   - Pull the throttle back to IDLE and touchdown with a maximum AOA of 13 degrees (green circle). More than 15 degrees AOA during the landing roll-out may cause the speedbrakes or engine nozzle to smash the runway (page 774).

4. **Aerodynamic Braking**:
   - Maintain a 13-degree nose-up attitude for a two-point aerodynamic braking until your airspeed has reduced to approximately 100 knots. This step is very important since the F-16’s brakes are not very effective (page 775).

5. **Landing Roll**:
   - Reduce back stick pressure and lower the nosewheel to the runway (page 775).
   - Open speedbrakes fully and maintain full aft stick for maximum braking effectiveness (page 775).
   - Apply moderate to heavy braking to slow the aircraft (page 775).
   - Engage nosewheel steering when below 30 knots and taxi off the runway (page 775). 

These steps will guide you through the ILS landing process in the F-16C.

**Holý LLM** (bez příručky):

> Performing an Instrument Landing System (ILS) approach and landing in the F-16C Viper involves several steps. Here’s a general guide to help you through the process:

### Pre-Flight Preparation
1. **Check the ILS Frequency**: Obtain the ILS frequency for your destination airport and set it in the radio navigation system (NAV) of the F-16C.
2. **Set the Course**: Set the inbound course (usually the runway heading) on the HSI (Horizontal Situation Indicator).

### Approach Setup
1. **Tune the ILS**: On the UFC (Up Front Controller), enter the ILS frequency into the NAV radio. Ensure that the ILS is active.
2. **Select the Approach Mode**: On the HSI, ensure that you have the ILS mode selected. This will allow you to receive the localizer and glideslope signals.
3. **Check the Weather**: Ensure that you have the appropriate weather conditions for an ILS approach.

### Descent and Approach
1. **Intercept the Localizer**: As you approach the airport, fly towards the localizer beam. You should see the localizer needle on the HSI. Adjust your heading to center the needle.
2. **Capture the Glideslope**: Once you are established on the localizer, descend to intercept the glideslope. The glideslope needle will indicate whether you are above or below the ideal descent path.
3. **Maintain Speed and Configuration**: Maintain a safe approach speed and configure the aircraft for landing (gear down, flaps as required).

### Final Approach
1. **Monitor the Instruments**: Keep an eye on the HSI and the altimeter. Make small adjustments to maintain the localizer and glideslope.
2. **Callouts**: Make altitude callouts as you descend through key altitudes (e.g., 1000 feet, 500 feet).
3. **Prepare for Landing**: As you approach the runway, ensure that you are stabilized on the glideslope and localizer.

### Landing
1. **Flare and Touchdown**: As you reach the runway threshold, begin your flare to reduce your descent rate. Touch down on the main gear first.
2. **Rollout**: After touchdown, apply brakes and use the rudder to maintain directional control on the runway.

### Post-Landing
1. **Taxi to Parking**: Once you have slowed down, taxi to your designated parking area.

### Additional Tips
- **Practice**: ILS approaches can be challenging, so practice in different weather conditions and scenarios.
- **Use the HUD**: The F-16C HUD provides valuable information during the approach, including altitude, speed, and guidance cues.
- **Stay Aware of Surroundings**: Always be aware of other traffic and any potential obstacles during your approach and landing.

By following these steps and practicing regularly, you will become proficient in performing ILS landings in the F-16C Viper module.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [OUT of corpus] How do I start the engines on the F/A-18C Hornet?

**Očekáváno** (strany []): Different aircraft not covered by this guide. The assistant should state the answer is not in the F-16 guide and not make it up.

**RAG** (našel strany [85, 90, 91, 118]):

> I cannot provide information on starting the engines of the F/A-18C Hornet, as the excerpts only cover the F-16C Viper.

**Holý LLM** (bez příručky):

> To start the engines on the F/A-18C Hornet in DCS, follow these steps:

1. **Power On**: Ensure the battery is on. You can do this by flipping the battery switch to the ON position.

2. **Fuel System**: Make sure the fuel system is set correctly. Check that the fuel pumps are on. You can do this by turning on the fuel boost pumps.

3. **Engine Start Switch**: Locate the engine start switch on the right side of the cockpit. Set the switch to the "START" position for the engine you want to start (either left or right).

4. **Monitor RPM**: Watch the engine RPM gauge. When the RPM reaches around 20%, you can move the engine start switch to the "RUN" position.

5. **Repeat for the Other Engine**: If you are starting both engines, repeat the process for the second engine.

6. **Check Engine Parameters**: After both engines are running, check the engine parameters (temperature, RPM, etc.) to ensure they are within normal operating ranges.

7. **Systems Check**: Once the engines are running, perform any necessary systems checks before taxiing.

Make sure to follow any specific procedures or checklists you have for the F/A-18C to ensure a safe and successful engine start.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [OUT of corpus] What is the real-world combat radius of the F-16 in kilometers?

**Očekáváno** (strany []): Real-world performance figure, not a DCS procedure from this guide. The assistant should say it is not in the guide.

**RAG** (našel strany [2, 174, 391, 8]):

> The excerpts do not provide information about the real-world combat radius of the F-16 in kilometers.

**Holý LLM** (bez příručky):

> The real-world combat radius of the F-16C Viper varies depending on the specific configuration, mission profile, and loadout. However, a general estimate for the combat radius of the F-16C is approximately 550 to 600 kilometers (about 340 to 370 miles) when carrying a typical loadout and flying at a moderate altitude. This range can be affected by factors such as fuel load, weapons, and mission type.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

## [OUT of corpus] How do I activate the IRST (infrared search and track) sensor on the F-16C?

**Očekáváno** (strany []): The DCS F-16C does not have an IRST; the guide does not cover it. The assistant should say the answer is not in the guide rather than inventing a procedure.

**RAG** (našel strany [273, 763, 192, 198]):

> The guide excerpts do not provide information on how to activate the IRST (infrared search and track) sensor on the F-16C.

**Holý LLM** (bez příručky):

> In the F-16C Viper module for DCS, the F-16C does not have an IRST (Infrared Search and Track) sensor as part of its standard avionics. The F-16C is primarily equipped with radar for target acquisition and tracking. 

If you are looking for infrared targeting capabilities, you would typically use the targeting pod (like the LANTIRN or Sniper pod) for visual identification and targeting of ground or air targets. To use such a pod, you would need to ensure it is properly loaded on the aircraft and then follow these general steps:

1. **Select the Targeting Pod**: Use the UFC (Up Front Controller) to select the targeting pod.
2. **Power On the Pod**: Ensure the pod is powered on and in the correct mode (e.g., IR mode).
3. **Use the TGP (Targeting Pod) Controls**: Use the TGP controls to designate targets and track them.

If you are looking for a specific feature or have a different module in mind that includes IRST capabilities, please clarify, and I can provide more detailed information.

**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  u 'mimo korpus' odmítl? ⬜

---

