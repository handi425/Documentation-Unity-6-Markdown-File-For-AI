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

#  [Tile](WSA.Tile.html).Update

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

public void Update(string xml);

## Declaration

public void Update(string medium, string wide, string large, string text);

### Parameters

xml | A string containing XML document for new tile look.  
---|---  
medium | An `uri` to 150x150 image, shown on medium tile.  
wide | An `uri` to a 310x150 image to be shown on a wide tile (if such issupported).  
large | An `uri` to a 310x310 image to be shown on a large tile (if such is supported).  
text | A text to shown on a tile.  
  
### Description

Send a notification for tile (update tiles look).

A tile is updated by providing and XML document with new look. The second
version is a convenience method to make tile display image, text or both. At
least one of medium and text argumets must be provided, and these two are used
to determine whether this is image-only, text-only or image-and-text tile.
Uris ms-appx:/// and ms-appdata://`local` can be used to access local
application resources. If uri points to network resource, internet access
capability must be enabled in applications manifest.

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

