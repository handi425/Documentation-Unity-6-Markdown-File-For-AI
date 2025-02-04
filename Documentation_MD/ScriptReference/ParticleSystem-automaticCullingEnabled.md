[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

**Removed**  

#  [ParticleSystem](ParticleSystem.html).automaticCullingEnabled

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

**Obsolete** automaticCullingEnabled property is deprecated. Use
proceduralSimulationSupported instead.  
**Upgrade to[proceduralSimulationSupported](ParticleSystem-
proceduralSimulationSupported.html)** public bool automaticCullingEnabled;

### Description

Does this system support Automatic Culling?

Internally, each Particle System has 2 modes of operating: procedural and non-
procedural.  
  
In procedural mode, it is possible to know the state of a Particle System for
any point in time (past and future) whereas a non-procedural system is
unpredictable. This means that it is possible to quickly fast forward (and
rewind) a procedural system to any point in time.  
  
When a system goes out of the view of any camera, it is culled. When this
occurs, the procedural system stops updating. It will efficiently fast forward
to the new point in time when the system becomes visible again. A non-
procedural system cannot do this, so it must continue updating itself even
when offscreen, due to its unpredictable nature.  
  
In order to support Automatic Culling, you can only use a subset of the
Particle System modules and properties. For example, using the Limit Velocity
over Lifetime module will disable Automatic Culling. Additionally, modifying
any properties from script whilst the system is playing will also disable
Automatic Culling.  
  
To discover if you are using any properties that disable this feature, a small
speech bubble appears in the upper right corner of the Inspector. The tooltip
for this icon gives you details about why Automatic Culling is disabled.

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

