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

# Scene

struct in UnityEngine.SceneManagement

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Run-time data structure for *.unity file.

### Properties

[buildIndex](SceneManagement.Scene-buildIndex.html)| Return the index of the
Scene in the Build Settings.  
---|---  
[isDirty](SceneManagement.Scene-isDirty.html)| Returns true if the Scene is
modified.  
[isLoaded](SceneManagement.Scene-isLoaded.html)| IsLoaded is set to true after
loading has completed and objects have been enabled.  
[name](SceneManagement.Scene-name.html)| Returns the name of the Scene that is
currently active in the game or app.  
[path](SceneManagement.Scene-path.html)| Returns the relative path of the
Scene. For example: "Assets/MyScenes/MyScene.unity".  
[rootCount](SceneManagement.Scene-rootCount.html)| The number of root
transforms of this Scene.  
  
### Public Methods

[GetRootGameObjects](SceneManagement.Scene.GetRootGameObjects.html)| Returns
all the root game objects in the Scene.  
---|---  
[IsValid](SceneManagement.Scene.IsValid.html)| Whether this is a valid Scene.
A Scene may be invalid if, for example, you tried to open a Scene that does
not exist. In this case, the Scene returned from EditorSceneManager.OpenScene
would return False for IsValid.  
  
### Operators

[operator !=](SceneManagement.Scene-operator_ne.html)| Returns true if the
Scenes are different.  
---|---  
[operator ==](SceneManagement.Scene-operator_eq.html)| Returns true if the
Scenes are equal.  
  
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

