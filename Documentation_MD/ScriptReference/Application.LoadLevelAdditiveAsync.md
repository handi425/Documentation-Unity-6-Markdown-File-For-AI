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

#  [Application](Application.html).LoadLevelAdditiveAsync

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

**Obsolete** Use SceneManager.LoadSceneAsync.

## Declaration

public static [AsyncOperation](AsyncOperation.html) LoadLevelAdditiveAsync(int
index);

**Obsolete** Use SceneManager.LoadSceneAsync.

## Declaration

public static [AsyncOperation](AsyncOperation.html)
LoadLevelAdditiveAsync(string levelName);

### Description

Loads the level additively and asynchronously in the background.

Unlike [LoadLevelAsync](Application.LoadLevelAsync.html),
LoadLevelAdditiveAsync does not destroy objects in the current level. Objects
from the new level are added to the current Scene. This is useful for creating
continuous virtual worlds, where more content is loaded in as you walk through
the environment.  
  
Unity will completely load all assets and all objects in the Scene in a
background loading thread. This allows you to create a completely streaming
world where you constantly load and unload different parts of the world based
on the player position, without any hiccups in game play.  
  
[isDone](AsyncOperation-isDone.html) variable from the resulting
[AsyncOperation](AsyncOperation.html) can be used to query if the level load
has completed. The result of a LoadLevelAdditiveAsync can also be used to
**yield** in a coroutine.  
  
When building a player Unity automatically optimizes assets in such a way that
LoadLevelAdditiveAsync will load them from disk linearly to avoid seek times.
Note that background loading performance in the Unity Editor is much lower
than in the standalone build. In the Editor you might also get more loading
hiccups than in the player.  
  
Refer to [Order of execution for event functions](../Manual/execution-
order.html) for more information regarding the calling sequence once a level
is loaded.  
  
Additional resources: [AsyncOperation](AsyncOperation.html),
[Application.backgroundLoadingPriority](Application-
backgroundLoadingPriority.html), Application.LoadLevelAdditive,
Application.LoadLevel, Application.LoadLevelAsync.

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

