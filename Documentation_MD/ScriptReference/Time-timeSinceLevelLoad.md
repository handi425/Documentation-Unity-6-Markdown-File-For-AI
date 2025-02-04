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

#  [Time](Time.html).timeSinceLevelLoad

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

public static float timeSinceLevelLoad;

### Description

The time in seconds since the last non-additive scene finished loading (Read
Only).

This behaves in the same way as [Time.time](Time-time.html) with a negative
offset.

    
    
    //Attach this script to a [GameObject](GameObject.html)
    //Create a [Button](UIElements.Button.html) (Create>UI>[Button](UIElements.Button.html)) and a Text [GameObject](GameObject.html) (Create>UI>Text)
    //Click on the [GameObject](GameObject.html) and attach the [Button](UIElements.Button.html) and Text in the fields in the Inspector  
      
    //This script outputs the time since the last level load. It also allows you to load a new [Scene](SceneManagement.Scene.html) by pressing the [Button](UIElements.Button.html). When this new [Scene](SceneManagement.Scene.html) loads, the time resets and updates.  
      
    using UnityEngine;
    using UnityEngine.SceneManagement;
    using UnityEngine.UI;  
      
    public class TimeSinceLevelLoad : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Button](UIElements.Button.html) m_MyButton;
        public Text m_MyText;  
      
        void Awake()
        {
            // Don't destroy the [GameObject](GameObject.html) when loading a new [Scene](SceneManagement.Scene.html)
            DontDestroyOnLoad(gameObject);
            // Make sure the [Canvas](Canvas.html) isn't deleted so the UI stays on the [Scene](SceneManagement.Scene.html) load
            DontDestroyOnLoad([GameObject.Find](GameObject.Find.html)("[Canvas](Canvas.html)"));  
      
            if (m_MyButton != null)
                // Add a listener to call the LoadSceneButton function when the [Button](UIElements.Button.html) is clicked
                m_MyButton.onClick.AddListener(LoadSceneButton);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Output the time since the [Scene](SceneManagement.Scene.html) loaded to the screen using this label
            m_MyText.text = "[Time](Time.html) Since Loaded : " + [Time.timeSinceLevelLoad](Time-timeSinceLevelLoad.html);
        }  
      
        void LoadSceneButton()
        {
            // Press this [Button](UIElements.Button.html) to load another [Scene](SceneManagement.Scene.html)
            // Load the [Scene](SceneManagement.Scene.html) named "Scene2"
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("Scene2");
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

