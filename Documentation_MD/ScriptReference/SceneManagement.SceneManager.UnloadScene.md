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

**Method group is Obsolete**  

#  [SceneManager](SceneManagement.SceneManager.html).UnloadScene

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

**Obsolete** Use SceneManager.UnloadSceneAsync. This function is not safe to
use during triggers and under other circumstances. See Scripting reference for
more details.

## Declaration

public static bool UnloadScene(int sceneBuildIndex);

**Obsolete** Use SceneManager.UnloadSceneAsync. This function is not safe to
use during triggers and under other circumstances. See Scripting reference for
more details.

## Declaration

public static bool UnloadScene(string sceneName);

**Obsolete** Use SceneManager.UnloadSceneAsync. This function is not safe to
use during triggers and under other circumstances. See Scripting reference for
more details.

## Declaration

public static bool
UnloadScene([SceneManagement.Scene](SceneManagement.Scene.html) scene);

### Parameters

sceneBuildIndex | Index of the Scene in the Build Settings to unload.  
---|---  
sceneName | Name or path of the Scene to unload.  
scene | Scene to unload.  
  
### Returns

**bool** Returns true if the Scene is unloaded.

### Description

Destroys all GameObjects associated with the given Scene and removes the Scene
from the SceneManager.

**Note:** It is not recommended to use this function but instead use
[UnloadSceneAsync](SceneManagement.SceneManager.UnloadSceneAsync.html).  
  
**Warning** : This cannot be called during various physics and visibility
callbacks like OnTriggerEnter or OnBecameVisible. This limitation is the
reason this function is not recommended to use.  
  
The given Scene name can either be the full Scene path, the path shown in the
Build Settings window or just the Scene name. If only the Scene name is given
this will load the first Scene in the list that matches. If you have multiple
Scenes with same name but different paths, you should use the full Scene path.
Examples of supported formats:  
`"Scene1"`  
`"Scene2"`  
`"Scenes/Scene3"`  
`"Scenes/Others/Scene3"`  
`"Assets/scenes/others/scene3.unity"`  
  
**Note:** sceneName is case insensitive.  
**Note:** Assets are currently not unloaded, in order to free up asset memory
call Resources.UnloadAllUnusedAssets.

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

