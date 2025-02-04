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

#  [Scene](SceneManagement.Scene.html).name

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

public string name;

### Description

Returns the name of the Scene that is currently active in the game or app.

The [Scene.name](Scene-name.html) returns a run-time, read-only, string value.
The [name](SceneManagement.Scene-name.html) limits to 244 characters. The
Scene name defaults to `scene`. The user changes the
[name](SceneManagement.Scene-name.html) during game creation.  
  
The following script example changes the Scene depending on
[GUI.Button](GUI.Button.html) clicks and the name of the Scene. To make this
example work:

  1. Create a Project with two Scenes, `scene1` and `scene2`.
  2. Attach the script below to a [GameObject](GameObject.html) added to `scene1`.
  3. Attach the same script to a [GameObject](GameObject.html) added to `scene2`.
  4. Click on the [GameObject](GameObject.html) and go to the Inspector.
  5. In the `My First Scene` field and `My Second Scene` fields, enter the names of the Scenes you would like to switch between, `scene1` and `scene2`.
  6. Select `scene1` by double-clicking it in the Project, and press `Play`. The `scene1` scene will appear.
  7. Click the `Load Next Scene` button and `scene2` will be loaded.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // These are the [Scene](SceneManagement.Scene.html) names. Make sure to set them in the Inspector window.
        public string myFirstScene, mySecondScene;  
      
        private string nextButton = "Load Next [Scene](SceneManagement.Scene.html)";
        private string nextScene;
        private static bool created = false;  
      
        private [Rect](Rect.html) buttonRect;
        private int width, height;  
      
        void Awake()
        {
            [Debug.Log](Debug.Log.html)("Awake:" + [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)().name);  
      
            // Ensure the script is not deleted while loading.
            if (!created)
            {
                DontDestroyOnLoad(this.gameObject);
                created = true;
            }
            else
            {
                Destroy(this.gameObject);
            }  
      
            // Specify the items for each scene.
            Camera.main.clearFlags = [CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html);
            width = [Screen.width](Screen-width.html);
            height = [Screen.height](Screen-height.html);
            buttonRect = new [Rect](Rect.html)(width / 8, height / 3, 3 * width / 4, height / 3);
        }  
      
        void OnGUI()
        {
            // Return the current Active [Scene](SceneManagement.Scene.html) in order to get the current [Scene](SceneManagement.Scene.html) name.
            [Scene](SceneManagement.Scene.html) scene = [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)();  
      
            // Check if the name of the current Active [Scene](SceneManagement.Scene.html) is your first [Scene](SceneManagement.Scene.html).
            if (scene.name == myFirstScene)
            {
                nextButton = "Load Next [Scene](SceneManagement.Scene.html)";
                nextScene = mySecondScene;
            }
            else
            {
                nextButton = "Load Previous [Scene](SceneManagement.Scene.html)";
                nextScene = myFirstScene;
            }  
      
            // [Display](Display.html) the button used to swap scenes.
            [GUIStyle](GUIStyle.html) buttonStyle = new [GUIStyle](GUIStyle.html)(GUI.skin.GetStyle("button"));
            buttonStyle.alignment = [TextAnchor.MiddleCenter](TextAnchor.MiddleCenter.html);
            buttonStyle.fontSize = 12 * (width / 200);  
      
            if ([GUI.Button](GUI.Button.html)(buttonRect, nextButton, buttonStyle))
            {
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)(nextScene);
            }
        }
    }
    

The following example using two scenes, and one of them has a long
[Scene](SceneManagement.Scene.html) name with 244 digits. The other is called
`testScene`. To make this example work:  
1\. Create a new Project.  
2\. Change the name of the default scene to `testScene` by selecting it and
then use Assets->Rename.  
3\. Next, create a second scene and again select it and use Asset->Rename. Use
the name as shown below. (This is the 244 character name "0123456789...0123").  
4\. Create a C# Script and call it `Example.cs`.  
5\. Add the following script text to `Example.cs`.  
6\. Next add an empty GameObject called `GameObject` to each of the two
scenes.  
7\. Finally copy `Example.cs` to each of the two GameObjects.  
Use the `Game` button to launch the `testScene` scene. A GUI Button is shown
which allows the scenes to swap.

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    // [SceneManagement.SceneManager](SceneManagement.SceneManager.html)-name example  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Scene](SceneManagement.Scene.html) scene;  
      
        void Start()
        {
            scene = [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)();
            [Debug.Log](Debug.Log.html)("Name: " + scene.name);
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 150, 100), "Change [Scene](SceneManagement.Scene.html)"))
            {
                if (scene.name == "testScene")
                {
                    // The scene to load has a 244 characters name.
                    [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("0123456789012345678901234567890123456789"
                        + "012345678901234567890123456789012345678901234567890123456789"
                        + "012345678901234567890123456789012345678901234567890123456789"
                        + "012345678901234567890123456789012345678901234567890123456789"
                        + "012345678901234567890123");
                }
                else
                {
                    [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("testScene");
                }
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

