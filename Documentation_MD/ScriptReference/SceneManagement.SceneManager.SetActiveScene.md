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

#  [SceneManager](SceneManagement.SceneManager.html).SetActiveScene

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

public static bool
SetActiveScene([SceneManagement.Scene](SceneManagement.Scene.html) scene);

### Parameters

scene | The Scene to be set.  
---|---  
  
### Returns

**bool** Returns false if the Scene is not loaded yet.

### Description

Set the Scene to be active.

The active Scene is the Scene which will be used as the target for new
GameObjects instantiated by scripts and from what Scene the lighting settings
are used. When you add a Scene additively (see
[LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html)), the
first Scene is still kept as the active Scene. Use this to switch the active
Scene to the Scene you want as the target.  
  
There must always be one Scene marked as the active Scene. Note the active
Scene has no impact on what Scenes are rendered.

    
    
    // Attach this script to a [GameObject](GameObject.html)
    // Create 2 Buttons (**Create** >**UI** >**Button**)
    // Attach the 2 Buttons to your [GameObject](GameObject.html)’s Inspector  
      
    // This script allows you to load a second [Scene](SceneManagement.Scene.html) as an Additive [Scene](SceneManagement.Scene.html). Click the first [Button](UIElements.Button.html) (Load [Scene](SceneManagement.Scene.html) [Button](UIElements.Button.html)) to load the Additive [Scene](SceneManagement.Scene.html). Even though the second [Scene](SceneManagement.Scene.html) loads, the first [Scene](SceneManagement.Scene.html) remains the active [Scene](SceneManagement.Scene.html).
    // If you press the second [Button](UIElements.Button.html) (Set Active [Button](UIElements.Button.html)), it sets the second [Scene](SceneManagement.Scene.html) as the active [Scene](SceneManagement.Scene.html) (and outputs the current active [Scene](SceneManagement.Scene.html) to the console)  
      
    
    using UnityEngine;
    using UnityEngine.SceneManagement;
    using UnityEngine.UI;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        bool m_SceneLoaded;
        public [Button](UIElements.Button.html) m_LoadSceneButton, m_SetActiveButton;  
      
        void Awake()
        {
            // Outputs the current active [Scene](SceneManagement.Scene.html) to the console
            [Debug.Log](Debug.Log.html)("Active [Scene](SceneManagement.Scene.html) : " + [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)().name);  
      
            // Check that this [Button](UIElements.Button.html) exists
            if (m_LoadSceneButton != null)
            {
                // Fetch the [Button](UIElements.Button.html) from the Inspector. Make sure to set this in the Inspector window
                [Button](UIElements.Button.html) loadButton = m_LoadSceneButton.GetComponent<[Button](UIElements.Button.html)>();  
      
                // Call the LoadScene2Button() function when this [Button](UIElements.Button.html) is clicked
                loadButton.onClick.AddListener(LoadSceneButton);
            }  
      
            if (m_SetActiveButton != null)
            {
                [Button](UIElements.Button.html) buttonTwo = m_SetActiveButton.GetComponent<[Button](UIElements.Button.html)>();
                buttonTwo.onClick.AddListener(SetActiveSceneButton);
            }
        }  
      
        // Load the [Scene](SceneManagement.Scene.html) when this [Button](UIElements.Button.html) is pressed
        void LoadSceneButton()
        {
            // Check that the second [Scene](SceneManagement.Scene.html) hasn't been added yet
            if (m_SceneLoaded == false)
            {
                // Loads the second [Scene](SceneManagement.Scene.html)
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("Scene2", [LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html));  
      
                // Outputs the name of the current active [Scene](SceneManagement.Scene.html).
                // Notice it still outputs the name of the first [Scene](SceneManagement.Scene.html)
                [Debug.Log](Debug.Log.html)("Active [Scene](SceneManagement.Scene.html) : " + [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)().name);  
      
                // The [Scene](SceneManagement.Scene.html) has been loaded, exit this method
                m_SceneLoaded = true;
            }
        }  
      
        // Change the newly loaded [Scene](SceneManagement.Scene.html) to be the active [Scene](SceneManagement.Scene.html) if it is loaded
        void SetActiveSceneButton()
        {
            // Allow this other [Button](UIElements.Button.html) to be pressed when the other [Button](UIElements.Button.html) has been pressed ([Scene](SceneManagement.Scene.html) 2 is loaded)
            if (m_SceneLoaded == true)
            {
                // Set Scene2 as the active [Scene](SceneManagement.Scene.html)
                [SceneManager.SetActiveScene](SceneManagement.SceneManager.SetActiveScene.html)([SceneManager.GetSceneByName](SceneManagement.SceneManager.GetSceneByName.html)("Scene2"));  
      
                // Ouput the name of the active [Scene](SceneManagement.Scene.html)
                // See now that the name is updated
                [Debug.Log](Debug.Log.html)("Active [Scene](SceneManagement.Scene.html) : " + [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)().name);
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

