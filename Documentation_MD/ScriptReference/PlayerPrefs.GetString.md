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

#  [PlayerPrefs](PlayerPrefs.html).GetString

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

public static string GetString(string key);

## Declaration

public static string GetString(string key, string defaultValue);

### Description

Returns the value corresponding to `key` in the preference file if it exists.

If it doesn't exist, PlayerPrefs.GetString will return `defaultValue`.

    
    
    //Use this script to fetch the settings and show them as text on the screen.  
      
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class PlayerPrefsGetStringExample : [MonoBehaviour](MonoBehaviour.html)
    {
        string m_PlayerName;  
      
        void Start()
        {
            //Fetch the PlayerPref settings
            SetText();
        }  
      
        void SetText()
        {
            //Fetch name (string) from the [PlayerPrefs](PlayerPrefs.html) (set these [PlayerPrefs](PlayerPrefs.html) in another script). If no string exists, the default is "No Name"
            m_PlayerName = [PlayerPrefs.GetString](PlayerPrefs.GetString.html)("Name", "No Name");
        }  
      
        void OnGUI()
        {
            //Fetch the [PlayerPrefs](PlayerPrefs.html) settings and output them to the screen using Labels
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(50, 50, 200, 30), "Name : " + m_PlayerName);
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

