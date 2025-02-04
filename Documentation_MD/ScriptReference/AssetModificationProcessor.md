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

# AssetModificationProcessor

class in UnityEditor

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

### Description

AssetModificationProcessor lets you hook into saving of serialized assets and
scenes which are edited inside Unity.

This lets you prevent writing of assets by Unity for integration with VCS
solutions like Perforce which require locking of files.  
  
This can be used as a callback to know when Assets are saved. You can then
make actions such as run code generator.

### Messages

[CanOpenForEdit](AssetModificationProcessor.CanOpenForEdit.html)| This is
called by Unity when inspecting assets to determine if they can potentially be
opened for editing.  
---|---  
[FileModeChanged](AssetModificationProcessor.FileModeChanged.html)| Unity
calls this method when file mode has been changed for one or more files.  
[IsOpenForEdit](AssetModificationProcessor.IsOpenForEdit.html)| This is called
by Unity when inspecting assets to determine if an editor should be disabled.  
[MakeEditable](AssetModificationProcessor.MakeEditable.html)| Unity calls this
method when one or more files need to be opened for editing.  
[OnWillCreateAsset](AssetModificationProcessor.OnWillCreateAsset.html)| Unity
calls this method when it is about to create an Asset you haven't imported
(for example, .meta files).  
[OnWillDeleteAsset](AssetModificationProcessor.OnWillDeleteAsset.html)| This
is called by Unity when it is about to delete an asset from disk.  
[OnWillMoveAsset](AssetModificationProcessor.OnWillMoveAsset.html)| Unity
calls this method when it is about to move an Asset on disk.  
[OnWillSaveAssets](AssetModificationProcessor.OnWillSaveAssets.html)| This is
called by Unity when it is about to write serialized assets or Scene files to
disk.  
  
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

