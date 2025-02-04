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

#  [Collider2D](Collider2D.html).contactCaptureLayers

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

public [LayerMask](LayerMask.html) contactCaptureLayers;

### Description

The layers of other [Collider2D](Collider2D.html) involved in contacts with
this [Collider2D](Collider2D.html) that will be captured.

Contacts are produced by the physics system and are used to calculate
behaviours such as collision response. These contacts are processed
automaticallly but they only need to be captured for performing physics
queries on them or to produce physics callbacks. Normally all contact layers
will be captured and stored, however this will result in increased processing
time and memory consumption. Selecting which layer(s) you are interested in
capturing can therefore increase performance and reduce overall memory
consumption however those layer(s) not captured will result in those contacts
not being available in physics queries and won't produce physics callbacks.  
  
By configuring the specific layer(s) you are interested in querying or
receiving callbacks for, you ensure you will only receive responses from
selected layer(s). This allows you to write more specific scripts as you can
assume that only specific layer(s) will be available.  
  
It is important to understand that the capture of contacts does not affect
collision response as contacts will always be handled by the physics system
before capture.  
  
These are the physics queries which require the capture of contacts:

  * [Physics2D.IsTouching](Physics2D.IsTouching.html)
  * [Rigidbody2D.IsTouching](Rigidbody2D.IsTouching.html)
  * [Collider2D.IsTouching](Collider2D.IsTouching.html),
  * [Physics2D.IsTouchingLayers](Physics2D.IsTouchingLayers.html)
  * [Rigidbody2D.IsTouchingLayers](Rigidbody2D.IsTouchingLayers.html)
  * [Collider2D.IsTouchingLayers](Collider2D.IsTouchingLayers.html),
  * [Physics2D.GetContacts](Physics2D.GetContacts.html)
  * [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
  * [Collider2D.GetContacts](Collider2D.GetContacts.html)

These are all the physics callbacks which require the capture of contacts:

  * [OnCollisionEnter2D](Collider2D.OnCollisionEnter2D.html)
  * [OnCollisionStay2D](Collider2D.OnCollisionStay2D.html)
  * [OnCollisionExit2D](Collider2D.OnCollisionExit2D.html)
  * [OnTriggerEnter2D](Collider2D.OnTriggerEnter2D.html)
  * [OnTriggerStay2D](Collider2D.OnTriggerStay2D.html)
  * [OnTriggerExit2D](Collider2D.OnTriggerExit2D.html)

**NOTES** :

  * This property does not control whether the [Collider2D](Collider2D.html) will come into contact or not but simply whether the resultant contacts are captured for querying and callbacks.
  * Even if all layers are selected in [Collider2D.callbackLayers](Collider2D-callbackLayers.html), only those that are captured will be reported.
  * Modifying contact capture layers will result in all contacts being destroyed. Contacts that are still valid will be reported as a new contacts via the physics callbacks.
  * Due to this property destroying existing contacts, it is not recommended that this property be changed during runtime if you are tracking contact state via physics callbacks.
  * Contacts are mutual therefore if either [Collider2D](Collider2D.html) involved in a contact disables capture of contacts then neither will see the contact.
  * With contact capture off for a layer, no contact queries will return results for that layer nor will any callbacks be produced.

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

