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

#
[MultiColumnHeaderState](IMGUI.Controls.MultiColumnHeaderState.html).OverwriteSerializedFields

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

## Declaration

public static void
OverwriteSerializedFields([IMGUI.Controls.MultiColumnHeaderState](IMGUI.Controls.MultiColumnHeaderState.html)
source,
[IMGUI.Controls.MultiColumnHeaderState](IMGUI.Controls.MultiColumnHeaderState.html)
destination);

### Parameters

source | State that have serialized data to be transfered to the destination state.  
---|---  
destination | Destination state.  
  
### Description

Overwrites the seralized fields from the source state to the destination
state.

Some of the fields in the MultiColumnHeader state are serializable so they can
be preserved between assembly reloads and/or when restarting Unity. The non-
serialized fields have to be reconstructed. After having reconstructed the
state use this method to apply any serialized fields from a previous session.
Ensure to check if the data can be overwritten using
[CanOverwriteSerializedFields](IMGUI.Controls.MultiColumnHeaderState.CanOverwriteSerializedFields.html)  
  
Additional resources:
[CanOverwriteSerializedFields](IMGUI.Controls.MultiColumnHeaderState.CanOverwriteSerializedFields.html).

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

