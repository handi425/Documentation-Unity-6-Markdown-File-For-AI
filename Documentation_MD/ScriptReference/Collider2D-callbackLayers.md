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

#  [Collider2D](Collider2D.html).callbackLayers

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

public [LayerMask](LayerMask.html) callbackLayers;

### Description

The Layers that this [Collider2D](Collider2D.html) will report collision or
trigger callbacks for during a contact with another
[Collider2D](Collider2D.html).

When a contact occurs between two [Collider2D](Collider2D.html), each
[Collider2D](Collider2D.html) will get a collision or trigger callback. This
options allows you to select which layer(s) will produce a callback.  
  
The ability to limit which layers will result in a callback can reduce the
complexity of the script inside the callback so that it can safely assume only
specific layers will be reported. There is also a performance benefit in not
performing callbacks that are not required.  
  
These are all the physics callbacks which are affected by callback layers:

  * [OnCollisionEnter2D](Collider2D.OnCollisionEnter2D.html)
  * [OnCollisionStay2D](Collider2D.OnCollisionStay2D.html)
  * [OnCollisionExit2D](Collider2D.OnCollisionExit2D.html)
  * [OnTriggerEnter2D](Collider2D.OnTriggerEnter2D.html)
  * [OnTriggerStay2D](Collider2D.OnTriggerStay2D.html)
  * [OnTriggerExit2D](Collider2D.OnTriggerExit2D.html)

**NOTES** :

  * This does not control whether the [Collider2D](Collider2D.html) will come into contact or not but simply if the resultant callback will happen.
  * Even if all callback layers are selected, only contacts captured via [Collider2D.contactCaptureLayers](Collider2D-contactCaptureLayers.html), will be reported.
  * The other [Collider2D](Collider2D.html) involved in any contact callback disabled here will still receive callbacks defined by its own [callbackLayers](Collider2D-callbackLayers.html) property.
  * Normally both the [Collider2D](Collider2D.html) and the [Rigidbody2D](Rigidbody2D.html) it is attached to receive a callback therefore this option controls both those component callbacks.
  * When enabling callback layers where callbacks already exist, those contacts will not be reported as new contacts i.e. there will not be an [OnCollisionEnter2D](Collider2D.OnCollisionEnter2D.html) or [OnTriggerEnter2D](Collider2D.OnTriggerEnter2D.html) callback produced.

Additional resources: [LayerMask](LayerMask.html).

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

