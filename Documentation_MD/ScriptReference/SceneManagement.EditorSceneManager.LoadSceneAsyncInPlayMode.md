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
[EditorSceneManager](SceneManagement.EditorSceneManager.html).LoadSceneAsyncInPlayMode

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

public static [AsyncOperation](AsyncOperation.html)
LoadSceneAsyncInPlayMode(string path,
[SceneManagement.LoadSceneParameters](SceneManagement.LoadSceneParameters.html)
parameters);

### Parameters

path | Path to Scene to load.  
---|---  
parameters | Parameters to apply to loading. See [LoadSceneParameters](SceneManagement.LoadSceneParameters.html).  
  
### Returns

**AsyncOperation** Use the [AsyncOperation](AsyncOperation.html) to determine
if the operation has completed.

### Description

This method allows you to load a Scene during playmode in the editor, without
requiring the Scene to be included in the [Build
Settings](../Manual/BuildSettings.html) Scene list.

The use case for this is to emulate Asset bundles while loading scenes in play
mode in the editor. When including a Scene in an asset bundle, you don't add
the Scene to build settings. This means you can't load the Scene during play
mode using the normal
[LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html) method.
Using this method instead of
[LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html) allows you
to load the Scene during play mode without requiring it to be in the Build
Settings Scene list. This means your code needs to detect whether the game is
[running in the editor](Application-isEditor.html) or not, and use this method
(LoadSceneAsyncInPlayMode) when in the editor, and
[LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html) when in the
built version.

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

