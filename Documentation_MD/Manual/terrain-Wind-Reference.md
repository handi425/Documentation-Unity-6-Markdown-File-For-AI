[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Wind-Reference.html)
  * [中文](/cn/current/Manual/terrain-Wind-Reference.html)
  * [日本語](/ja/current/Manual/terrain-Wind-Reference.html)
  * [한국어](/kr/current/Manual/terrain-Wind-Reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Wind-Reference.html)
  * [中文](/cn/current/Manual/terrain-Wind-Reference.html)
  * [日本語](/ja/current/Manual/terrain-Wind-Reference.html)
  * [한국어](/kr/current/Manual/terrain-Wind-Reference.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Animate trees with Wind Zones](class-WindZone.html)
  * Wind reference

[](class-WindZone.html)

Animate trees with Wind Zones

[](terrain-Grass.html)

Grass and other details

# Wind reference

**Property** | **Function** |   
---|---|---  
**Mode**  
| **Directional** | The **Wind Zone** A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](class-WindZone.html)  
See in [Glossary](Glossary.html#windzone) affects the entire **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and blows in one direction. This is the
default mode.  
| **Spherical** | The Wind Zone only has an effect inside the radius, and has a falloff from the center towards the edge.  
**Radius** | Wind Zone size (active only if the mode is Spherical).  
**Main** | The primary force applied to all objects the Wind Zone affects. The numerical value is the wind speed; the plus and minus signs are the direction. If the value is 0, but **Turbulence** has a value other than 0, the trees still move. If both **Main** and **Turbulence** are 0, the trees bend, but they don’t move - they stay in a static bent position.  
**Turbulence** | Represents the noise applied to the wind speed. A greater value creates higher variation in wind speed. If **Turbulence** isn’t 0, there’s wind even if **Main** is 0. If **Turbulence** is 0, there’s no wind even if **Main** has a value other than 0.  
**Pulse Magnitude** | Pulses create the appearance of gusts of wind that are stronger than the main wind. **Magnitude** is a multiplier of **Main** , meaning if **Main** and **Turbulence** are both 0 the pulses are also 0.  
**Pulse Frequency** | How frequent pulses are, and how long they last. More frequent pulses are shorter.  
  
## Additional resources

  * [Animate trees with Wind Zones](class-WindZone.html)
  * [Terrain Settings reference](terrain-OtherSettings.html)

[](class-WindZone.html)

Animate trees with Wind Zones

[](terrain-Grass.html)

Grass and other details

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

