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

#  [Rigidbody2D](Rigidbody2D.html).includeLayers

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

[ ]()

public [LayerMask](LayerMask.html) includeLayers;

### Description

The additional Layers that all [Collider2D](Collider2D.html) attached to this
[Rigidbody2D](Rigidbody2D.html) should include when deciding if a contact with
another [Collider2D](Collider2D.html) should happen or not.

The Layer Collision Matrix defines which Layers can and cannot contact other
Layers. This property allows you to specify additional Layers that all
[Collider2D](Collider2D.html) attached to this [Rigidbody2D](Rigidbody2D.html)
instance can contact.  
  
**NOTE** : Because Layers can be included or excluded differently depending on
the settings of each [Collider2D](Collider2D.html) instance, there is the
potential for a conflicting decision for whether contact should happen or not
when two [Collider2D](Collider2D.html) instances come into contact with each
other. You can find the detailed rules for how Unity arbitrates this decision
in the
[Collider2D.layerOverridePriority](Collider2D-layerOverridePriority.html)
documentation.  
  
Additional resources:
[Rigidbody2D.excludeLayers](Rigidbody2D-excludeLayers.html),
[Collider2D.includeLayers](Collider2D-includeLayers.html) &
[Collider2D.excludeLayers](Collider2D-excludeLayers.html).

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

