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

#  [Physics](Physics.html).autoSyncTransforms

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

public static bool autoSyncTransforms;

### Description

Whether or not to automatically sync transform changes with the physics system
whenever a [Transform](Transform.html) component changes.

When a [Transform](Transform.html) component changes, any
[Rigidbody](Rigidbody.html) or [Collider](Collider.html) on that
[Transform](Transform.html) or its children may need to be repositioned,
rotated or scaled depending on the change to the [Transform](Transform.html).
You can control if the changes made to the [Transform](Transform.html) are
automatically applied to the correct components by setting this property true.
When set to false, synchronization only occurs prior to the physics simulation
step during the Fixed Update. You can also manually synchronize transform
changes using [Physics.SyncTransforms](Physics.SyncTransforms.html).  
  
**Note** : When autoSyncTransforms is set to true, repeatedly changing a
Transform and then performing a physics query can cause performance loss. To
avoid affecting performance, set autoSyncTransforms to false if you want to
perform multiple Transform changes and queries in succession. You should only
set autoSyncTransforms to true for physics backwards compatibility in existing
projects made before Unity 2017.2. For projects made in Unity 2017.2 onwards,
turn this option off.

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

