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

#  [PlayerPrefs](PlayerPrefs.html).DeleteAll

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

public static void DeleteAll();

### Description

Removes all keys and values from the preferences. Use with caution.

Call this function in a script to delete all current settings in the
[PlayerPrefs](PlayerPrefs.html).  
  
The following example demonstrates creating a button that deletes all
PlayerPrefs.

    
    
    //This example creates a button on the screen that deletes any [PlayerPrefs](PlayerPrefs.html) settings when you press it.
    //Note that you must set values or keys in the [PlayerPrefs](PlayerPrefs.html) first to see the button.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            //Delete all of the [PlayerPrefs](PlayerPrefs.html) settings by pressing this button.
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 200, 200, 60), "Delete"))
            {
                [PlayerPrefs.DeleteAll](PlayerPrefs.DeleteAll.html)();
            }
        }
    }
    

The following example demonstrates setting PlayerPrefs and deleting them
afterwards.

    
    
    //First attach this script to a [GameObject](GameObject.html) in the [Scene](SceneManagement.Scene.html) to set up the [PlayerPrefs](PlayerPrefs.html).  
      
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class SetUpPlayerPrefsExample : [MonoBehaviour](MonoBehaviour.html)
    {
        string m_PlayerName;  
      
        void Start()
        {
            m_PlayerName = "Enter Your Name";
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Give the [PlayerPrefs](PlayerPrefs.html) some values to send over to the next [Scene](SceneManagement.Scene.html)
            [PlayerPrefs.SetFloat](PlayerPrefs.SetFloat.html)("Health", 50.0F);
            [PlayerPrefs.SetInt](PlayerPrefs.SetInt.html)("Score", 20);
            [PlayerPrefs.SetString](PlayerPrefs.SetString.html)("Name", m_PlayerName);
        }  
      
        void OnGUI()
        {
            //Create a Text Field where the user inputs their name
            m_PlayerName = [GUI.TextField](GUI.TextField.html)(new [Rect](Rect.html)(10, 10, 200, 20), m_PlayerName, 25);  
      
            //Create a button which loads the appropriate level when you press it
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 30, 200, 60), "Next [Scene](SceneManagement.Scene.html)"))
            {
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("Scene2");
            }
        }
    }
    
    
    
    //This other script shows how the values of the [PlayerPrefs](PlayerPrefs.html) reset using the [PlayerPrefs.DeleteAll](PlayerPrefs.DeleteAll.html)() function.
    //Open a different [Scene](SceneManagement.Scene.html) (the one you named before- "Scene2") and attach this script to a new [GameObject](GameObject.html).
    //Use this script to fetch the settings and show them as text on the screen.
    //Use the button included in the script to delete all these settings and the text on the screen will also reset to reflect this.  
      
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class PlayerPrefsDeleteAllExample : [MonoBehaviour](MonoBehaviour.html)
    {
        int m_Score;
        float m_Health;
        string m_PlayerName;  
      
        void Start()
        {
            //Fetch the PlayerPref settings
            SetText();
        }  
      
        void SetText()
        {
            //Fetch the score, health and name from the [PlayerPrefs](PlayerPrefs.html) (set these Playerprefs in another script)
            m_Health = [PlayerPrefs.GetFloat](PlayerPrefs.GetFloat.html)("Health", 0);
            m_Score = [PlayerPrefs.GetInt](PlayerPrefs.GetInt.html)("Score", 0);
            m_PlayerName = [PlayerPrefs.GetString](PlayerPrefs.GetString.html)("Name", "No Name");
        }  
      
        void OnGUI()
        {
            //Fetch the [PlayerPrefs](PlayerPrefs.html) settings and output them to the screen using Labels
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(50, 50, 200, 30), "Name : " + m_PlayerName);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(50, 90, 200, 30), "Health : " + m_Health);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(50, 130, 200, 30), "Score : " + m_Score);  
      
            //Delete all of the [PlayerPrefs](PlayerPrefs.html) settings by pressing this [Button](UIElements.Button.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(50, 0, 100, 30), "Delete"))
            {
                [PlayerPrefs.DeleteAll](PlayerPrefs.DeleteAll.html)();
                //Fetch the updated settings to change the Text
                SetText();
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

