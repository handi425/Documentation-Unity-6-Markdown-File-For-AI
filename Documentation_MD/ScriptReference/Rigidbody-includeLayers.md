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

#  [Rigidbody](Rigidbody.html).includeLayers

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

[Switch to Manual](../Manual/class-Rigidbody.html "Go to Rigidbody Component
in the Manual")

public [LayerMask](LayerMask.html) includeLayers;

### Description

The additional layers that all [Collider](Collider.html)s attached to this
[Rigidbody](Rigidbody.html) should include when deciding if the
[Collider](Collider.html) can come into contact with another
[Collider](Collider.html).

The Layer Collision Matrix defines which layers can contact other layers. Use
this property to specify additional layers that all [Collider](Collider.html)s
attached to this [Rigidbody](Rigidbody.html) instance can contact.  
  
**NOTE** : Layers can be included or excluded differently depending on the
settings of each [Collider](Collider.html) instance. As such, there could be a
conflicting decision for whether two [Collider](Collider.html) instances can
come into contact with each other. To learn how Unity decides this, see
[Collider.layerOverridePriority](Collider-layerOverridePriority.html).  
  
Additional resources: [Collider.excludeLayers](Collider-excludeLayers.html),
[Rigidbody.excludeLayers](Rigidbody-excludeLayers.html),
[ArticulationBody.includeLayers](ArticulationBody-includeLayers.html),
[ArticulationBody.excludeLayers](ArticulationBody-excludeLayers.html).

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

