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

#  [LoadSceneMode](SceneManagement.LoadSceneMode.html).Single

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

Closes all current loaded Scenes and loads a Scene.

Additional resources:
[SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html).

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            //This displays a [Button](UIElements.Button.html) on the screen at position (20,30), width 150 and height 50. The button’s text reads the last parameter. Press this for the [SceneManager](SceneManagement.SceneManager.html) to load the [Scene](SceneManagement.Scene.html).
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(20, 30, 150, 30), "Other [Scene](SceneManagement.Scene.html) Single"))
            {
                //The [SceneManager](SceneManagement.SceneManager.html) loads your new [Scene](SceneManagement.Scene.html) as a single [Scene](SceneManagement.Scene.html) (not overlapping). This is Single mode.
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("YourScene", [LoadSceneMode.Single](SceneManagement.LoadSceneMode.Single.html));
            }  
      
            //Whereas pressing this [Button](UIElements.Button.html) loads the Additive [Scene](SceneManagement.Scene.html).
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(20, 60, 150, 30), "Other [Scene](SceneManagement.Scene.html) Additive"))
            {
                //[SceneManager](SceneManagement.SceneManager.html) loads your new [Scene](SceneManagement.Scene.html) as an extra [Scene](SceneManagement.Scene.html) (overlapping the other). This is Additive mode.
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("YourScene", [LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html));
            }
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

