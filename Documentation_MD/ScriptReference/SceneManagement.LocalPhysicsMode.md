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

# LocalPhysicsMode

enumeration

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

Provides options for 2D and 3D local physics.

By default, when a [Scene](SceneManagement.Scene.html) is created or loaded,
any 2D or 3D physics component added to a GameObject within the Scene is added
to the default physics Scene. Each [Scene](SceneManagement.Scene.html) however
has the ability to create and own its own (local) 2D and/or 3D physics Scene.
This option can be used when creating or loading a Scene to specify whether a
2D and/or 3D physics Scene should be created.  
  
When a [Scene](SceneManagement.Scene.html) creates its own 2D and/or 3D
physics Scene, the lifetime of the physics Scene(s) is the same as the
[Scene](SceneManagement.Scene.html) i.e. if the
[Scene](SceneManagement.Scene.html) is destroyed/unloaded then so are any
created physics Scenes.  
  
Additional resources:
[CreateSceneParameters](SceneManagement.CreateSceneParameters.html),
[LoadSceneParameters](SceneManagement.LoadSceneParameters.html),
[SceneManager.CreateScene](SceneManagement.SceneManager.CreateScene.html),
[SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html) and
[SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html).

### Properties

[None](SceneManagement.LocalPhysicsMode.None.html)| No local 2D or 3D physics
Scene will be created.  
---|---  
[Physics2D](SceneManagement.LocalPhysicsMode.Physics2D.html)| A local 2D
physics Scene will be created and owned by the Scene.  
[Physics3D](SceneManagement.LocalPhysicsMode.Physics3D.html)| A local 3D
physics Scene will be created and owned by the Scene.  
  
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

