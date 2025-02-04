[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-TimeManager.html)
  * [中文](/cn/current/Manual/class-TimeManager.html)
  * [日本語](/ja/current/Manual/class-TimeManager.html)
  * [한국어](/kr/current/Manual/class-TimeManager.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-TimeManager.html)
  * [中文](/cn/current/Manual/class-TimeManager.html)
  * [日本語](/ja/current/Manual/class-TimeManager.html)
  * [한국어](/kr/current/Manual/class-TimeManager.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Project Settings](comp-ManagerGroup.html)
  * Time

[](class-TagManager.html)

Tags and Layers

[](UIB-project-setting.html)

UI Toolkit project settings

# Time

The **Time** settings (menu: **Edit > Project Settings**, then the _Time_
category) lets you set a number of properties that control timing within your
game.

![](../uploads/Main/TimeSet.png)

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Fixed Timestep** | A frame-rate-independent interval that dictates when physics calculations and **FixedUpdate()** events are performed.  
**Maximum Allowed Timestep** | A frame-rate-independent interval that caps the worst case scenario when frame-rate is low. Physics calculations and **FixedUpdate()** events will not be performed for longer time than specified.  
**Time Scale** | The speed at which time progresses. Change this value to simulate bullet-time effects. A value of 1 means real-time. A value of .5 means half speed; a value of 2 is double speed.  
**Maximum Particle Timestep** | A frame-rate-independent interval that controls the accuracy of the particle simulation. When the frame time exceeds this value, multiple iterations of the particle update are performed in one frame, so that the duration of each step does not exceed this value. For example, a game running at 30fps (0.03 seconds per frame) could run the particle update at 60fps (in steps of 0.0167 seconds) to achieve a more accurate simulation, at the expense of performance.  
  
## Details

The **Time Manager** lets you set properties globally, but it is often useful
to set them from a script during gameplay (for example, setting **Time Scale**
to zero is a useful way to pause the game). Refer to the page on [Time and
frame rate management](managing-time-and-frame-rate.html) for full details of
how time can be managed in Unity.

* * *

2017–05–18 Page published

**Maximum Particle Timestep** added in
[2017.1](https://docs.unity3d.com/2017.1/Documentation/Manual/30_search.html?q=newin20171)
NewIn20171

TimeManager

[](class-TagManager.html)

Tags and Layers

[](UIB-project-setting.html)

UI Toolkit project settings

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

