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

#  [PlayerSettings](PlayerSettings.html).defaultWebScreenHeight

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

public static int defaultWebScreenHeight;

### Description

Default vertical dimension of web player window.

![](../StaticFiles/ScriptRefImages/PlayerSettingsCustomSettings.png)  
_Custom player settings._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Simple Script that saves and loads custom
    // Stand-alone/Web player screen settings among
    // Unity Projects  
      
    class CustomSettings : [EditorWindow](EditorWindow.html)
    {  
      
        string compName = "";
        string prodName = "";
        int screenWidth = 640;
        int screenHeight = 480;
        int webScreenWidth = 640;
        int webScreenHeight = 480;
        bool fullScreen = false;  
      
        [[MenuItem](MenuItem.html)("Examples/Custom [Settings](CameraEditor.Settings.html)")]
            static void Init()
        {
            var window = GetWindow<CustomSettings>();
            window.Show();
        }  
      
        void OnGUI()
        {
            compName = [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("Company Name:", compName);
            prodName = [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("Product Name:", prodName);
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            screenWidth = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Width:", screenWidth);
            screenHeight = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Web Height:", screenHeight);
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
            [EditorGUILayout.Space](EditorGUILayout.Space.html)();
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            webScreenWidth = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Web Width:", webScreenWidth);
            webScreenHeight = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Web Height:", webScreenHeight);
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
            fullScreen = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Full [Screen](Screen.html):", fullScreen);
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            if ([GUILayout.Button](GUILayout.Button.html)("Save Values"))
                SaveSettings();
            if ([GUILayout.Button](GUILayout.Button.html)("Load Values"))
                LoadSettings();
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
        }  
      
        void SaveSettings()
        {
            [PlayerSettings.companyName](PlayerSettings-companyName.html) = compName;
            [PlayerSettings.productName](PlayerSettings-productName.html) = prodName;
            [PlayerSettings.defaultScreenWidth](PlayerSettings-defaultScreenWidth.html) = screenWidth;
            [PlayerSettings.defaultScreenHeight](PlayerSettings-defaultScreenHeight.html) = screenHeight;
            [PlayerSettings.defaultWebScreenWidth](PlayerSettings-defaultWebScreenWidth.html) = webScreenWidth;
            [PlayerSettings.defaultWebScreenHeight](PlayerSettings-defaultWebScreenHeight.html) = webScreenHeight;
            PlayerSettings.defaultIsFullScreen = fullScreen;  
      
            [EditorPrefs.SetString](EditorPrefs.SetString.html)("CompName", compName);
            [EditorPrefs.SetString](EditorPrefs.SetString.html)("ProdName", prodName);
            [EditorPrefs.SetInt](EditorPrefs.SetInt.html)("ScreenWidth", screenWidth);
            [EditorPrefs.SetInt](EditorPrefs.SetInt.html)("ScreenHeight", screenHeight);
            [EditorPrefs.SetInt](EditorPrefs.SetInt.html)("WebScreenWidth", webScreenWidth);
            [EditorPrefs.SetInt](EditorPrefs.SetInt.html)("WebScreenHeight", webScreenHeight);
        }
        void LoadSettings()
        {
            compName = [EditorPrefs.GetString](EditorPrefs.GetString.html)("CompName", "");
            prodName = [EditorPrefs.GetString](EditorPrefs.GetString.html)("ProdName", "");
            screenWidth = [EditorPrefs.GetInt](EditorPrefs.GetInt.html)("ScreenWidth", 640);
            screenHeight = [EditorPrefs.GetInt](EditorPrefs.GetInt.html)("ScreenHeight", 480);
            webScreenWidth = [EditorPrefs.GetInt](EditorPrefs.GetInt.html)("WebScreenWidth", 640);
            webScreenHeight = [EditorPrefs.GetInt](EditorPrefs.GetInt.html)("WebScreenHeight", 480);
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

