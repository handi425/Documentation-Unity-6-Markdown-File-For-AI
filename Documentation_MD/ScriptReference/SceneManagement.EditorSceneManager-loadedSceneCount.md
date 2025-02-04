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

#
[EditorSceneManager](SceneManagement.EditorSceneManager.html).loadedSceneCount

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

**Obsolete** EditorSceneManager.loadedSceneCount has been deprecated. Please
use SceneManager.loadedSceneCount.  
**Upgrade to[loadedSceneCount](SceneManagement.SceneManager-
loadedSceneCount.html)** public static int loadedSceneCount;

### Description

The number of loaded Scenes.

Returns the current number of loaded Scenes in the Editor. The difference
between loadedSceneCount and
[SceneManager.sceneCount](SceneManagement.SceneManager-sceneCount.html) is for
scenes that are shown in the Hierarchy but are unloaded.
[SceneManager.sceneCount](SceneManagement.SceneManager-sceneCount.html) counts
those scenes, but loadedSceneCount does not.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SceneManagement;  
      
    public class Example
    {
        // adds a custom menu item which displays the number of open Scenes in a Dialogue [Box](UIElements.Box.html)
        [[MenuItem](MenuItem.html)("SceneExample/Number Of Scenes")]
        public static void NumberOfScenes()
        {
            [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("Number of loaded Scenes:", EditorSceneManager.loadedSceneCount.ToString(), "OK");
        }
    }
    

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

