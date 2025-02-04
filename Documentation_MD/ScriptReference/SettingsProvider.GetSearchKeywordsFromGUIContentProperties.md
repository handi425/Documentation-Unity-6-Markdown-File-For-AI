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

#
[SettingsProvider](SettingsProvider.html).GetSearchKeywordsFromGUIContentProperties

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

public static IEnumerable<string> GetSearchKeywordsFromGUIContentProperties();

### Returns

**IEnumerable <string>** Returns the list of keywords extracted from the
static GUIContent.

### Description

Extract search keywords from all public static memebers in a specific Type.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Create a new type of [Settings](CameraEditor.Settings.html) asset.
    class MyCustomSettings : [ScriptableObject](ScriptableObject.html)
    {
        public const string k_MyCustomSettingsPath = "Assets/[Editor](Editor.html)/MyCustomSettings.asset";  
      
        [[SerializeField](SerializeField.html)]
        private int m_Number;  
      
        [[SerializeField](SerializeField.html)]
        private string m_SomeString;  
      
        internal static MyCustomSettings GetOrCreateSettings()
        {
            var settings = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<MyCustomSettings>(k_MyCustomSettingsPath);
            if (settings == null)
            {
                settings = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MyCustomSettings>();
                settings.m_Number = 42;
                settings.m_SomeString = "The answer to the universe";
                [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(settings, k_MyCustomSettingsPath);
                [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();
            }
            return settings;
        }  
      
        internal static [SerializedObject](SerializedObject.html) GetSerializedSettings()
        {
            return new [SerializedObject](SerializedObject.html)(GetOrCreateSettings());
        }
    }  
      
    class AssetSettingsProviderRegister
    {
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateFromFilePath()
        {
            // Create an [AssetSettingsProvider](AssetSettingsProvider.html) from a file path:
            var provider = [AssetSettingsProvider.CreateProviderFromAssetPath](AssetSettingsProvider.CreateProviderFromAssetPath.html)("Project/AssetSettings/FromFile", MyCustomSettings.k_MyCustomSettingsPath);  
      
            // Register keywords from the properties of the serialized object at a specific path
            provider.keywords = [SettingsProvider.GetSearchKeywordsFromPath](SettingsProvider.GetSearchKeywordsFromPath.html)(MyCustomSettings.k_MyCustomSettingsPath);
            return provider;
        }  
      
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateFromSettingsObject()
        {
            // Create an [AssetSettingsProvider](AssetSettingsProvider.html) from a settings object (UnityEngine.Object):
            var settingsObj = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath);
            var provider = [AssetSettingsProvider.CreateProviderFromObject](AssetSettingsProvider.CreateProviderFromObject.html)("Project/AssetSettings/FromObject", settingsObj);  
      
            // Register keywords from the properties of settingsObj
            provider.keywords = [SettingsProvider.GetSearchKeywordsFromSerializedObject](SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new [SerializedObject](SerializedObject.html)(settingsObj));
            return provider;
        }  
      
        class Styles
        {
            public static [GUIContent](GUIContent.html) number = new [GUIContent](GUIContent.html)("My Number");
            public static [GUIContent](GUIContent.html) someString = new [GUIContent](GUIContent.html)("Some string");
        }  
      
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateFromSettingsFromFunctor()
        {
            // Create an [AssetSettingsProvider](AssetSettingsProvider.html) from a functor that must returns a UnityEngine.Object:
            var provider = new [AssetSettingsProvider](AssetSettingsProvider.html)("Project/AssetSettings/FromFunctor", () => UnityEditor.Editor.CreateEditor([AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath)));  
      
            // Register keywords from the static [GUIContent](GUIContent.html) in Styles class
            provider.keywords = [SettingsProvider.GetSearchKeywordsFromGUIContentProperties](SettingsProvider.GetSearchKeywordsFromGUIContentProperties.html)<Styles>();
            return provider;
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

