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

# SettingsProvider Constructor

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

public SettingsProvider(string path, [SettingsScope](SettingsScope.html)
scopes, IEnumerable<string> keywords);

### Parameters

path | Path of the settings in the Settings window. Uses "/" as separator. The last token becomes the settings label if none is provided.  
---|---  
scope | Scope of the Settings. The Scope determines where the setting appears: in the Settings or the Preferences windows.  
keywords | List of keywords to compare against what the user is searching for. When the user enters values in the search box on the Settings window, [SettingsProvider.HasSearchInterest](SettingsProvider.HasSearchInterest.html) tries to match those keywords to this list.  
  
### Description

Creates a new SettingsProvider.

    
    
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;
    using UnityEditor.UIElements;  
      
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
      
    // Register a [SettingsProvider](SettingsProvider.html) using IMGUI for the drawing framework:
    static class MyCustomSettingsIMGUIRegister
    {
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateMyCustomSettingsProvider()
        {
            // First parameter is the path in the [Settings](CameraEditor.Settings.html) window.
            // Second parameter is the scope of this setting: it only appears in the Project [Settings](CameraEditor.Settings.html) window.
            var provider = new [SettingsProvider](SettingsProvider.html)("Project/MyCustomIMGUISettings", [SettingsScope.Project](SettingsScope.Project.html))
            {
                // By default the last token of the path is used as display name if no label is provided.
                label = "Custom IMGUI",
                // Create the [SettingsProvider](SettingsProvider.html) and initialize its drawing (IMGUI) function in place:
                guiHandler = (searchContext) =>
                {
                    var settings = MyCustomSettings.GetSerializedSettings();
                    [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(settings.FindProperty("m_Number"), new [GUIContent](GUIContent.html)("My Number"));
                    [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(settings.FindProperty("m_SomeString"), new [GUIContent](GUIContent.html)("My String"));
                    settings.ApplyModifiedPropertiesWithoutUndo();
                },  
      
                // Populate the search keywords to enable smart search filtering and label highlighting:
                keywords = new HashSet<string>(new[] { "Number", "Some String" })
            };  
      
            return provider;
        }
    }  
      
    // Register a [SettingsProvider](SettingsProvider.html) using UIElements for the drawing framework:
    static class MyCustomSettingsUIElementsRegister
    {
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateMyCustomSettingsProvider()
        {
            // First parameter is the path in the [Settings](CameraEditor.Settings.html) window.
            // Second parameter is the scope of this setting: it only appears in the [Settings](CameraEditor.Settings.html) window for the Project scope.
            var provider = new [SettingsProvider](SettingsProvider.html)("Project/MyCustomUIElementsSettings", [SettingsScope.Project](SettingsScope.Project.html))
            {
                label = "Custom UI Elements",
                // activateHandler is called when the user clicks on the [Settings](CameraEditor.Settings.html) item in the [Settings](CameraEditor.Settings.html) window.
                activateHandler = (searchContext, rootElement) =>
                {
                    var settings = MyCustomSettings.GetSerializedSettings();  
      
                    // rootElement is a [VisualElement](UIElements.VisualElement.html). If you add any children to it, the OnGUI function
                    // isn't called because the [SettingsProvider](SettingsProvider.html) uses the UIElements drawing framework.
                    var styleSheet = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[StyleSheet](UIElements.StyleSheet.html)>("Assets/[Editor](Editor.html)/settings_ui.uss");
                    rootElement.styleSheets.Add(styleSheet);
                    var title = new [Label](UIElements.Label.html)()
                    {
                        text = "Custom UI Elements"
                    };
                    title.AddToClassList("title");
                    rootElement.Add(title);  
      
                    var properties = new [VisualElement](UIElements.VisualElement.html)()
                    {
                        style =
                        {
                            flexDirection = [FlexDirection.Column](UIElements.FlexDirection.Column.html)
                        }
                    };
                    properties.AddToClassList("property-list");
                    rootElement.Add(properties);  
      
                    properties.Add(new [PropertyField](UIElements.PropertyField.html)(settings.FindProperty("m_SomeString")));
                    properties.Add(new [PropertyField](UIElements.PropertyField.html)(settings.FindProperty("m_Number")));  
      
                    rootElement.Bind(settings);
                },  
      
                // Populate the search keywords to enable smart search filtering and label highlighting:
                keywords = new HashSet<string>(new[] { "Number", "Some String" })
            };  
      
            return provider;
        }
    }  
      
    // Create MyCustomSettingsProvider by deriving from [SettingsProvider](SettingsProvider.html):
    class MyCustomSettingsProvider : [SettingsProvider](SettingsProvider.html)
    {
        private [SerializedObject](SerializedObject.html) m_CustomSettings;  
      
        class Styles
        {
            public static [GUIContent](GUIContent.html) number = new [GUIContent](GUIContent.html)("My Number");
            public static [GUIContent](GUIContent.html) someString = new [GUIContent](GUIContent.html)("Some string");
        }  
      
        const string k_MyCustomSettingsPath = "Assets/[Editor](Editor.html)/MyCustomSettings.asset";
        public MyCustomSettingsProvider(string path, [SettingsScope](SettingsScope.html) scope = [SettingsScope.User](SettingsScope.User.html))
            : base(path, scope) {}  
      
        public static bool IsSettingsAvailable()
        {
            return [File.Exists](Windows.File.Exists.html)(k_MyCustomSettingsPath);
        }  
      
        public override void OnActivate(string searchContext, [VisualElement](UIElements.VisualElement.html) rootElement)
        {
            // This function is called when the user clicks on the MyCustom element in the [Settings](CameraEditor.Settings.html) window.
            m_CustomSettings = MyCustomSettings.GetSerializedSettings();
        }  
      
        public override void OnGUI(string searchContext)
        {
            // Use IMGUI to display UI:
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_CustomSettings.FindProperty("m_Number"), Styles.number);
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_CustomSettings.FindProperty("m_SomeString"), Styles.someString);
            m_CustomSettings.ApplyModifiedPropertiesWithoutUndo();
        }  
      
        // Register the [SettingsProvider](SettingsProvider.html)
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateMyCustomSettingsProvider()
        {
            if (IsSettingsAvailable())
            {
                var provider = new MyCustomSettingsProvider("Project/MyCustomSettingsProvider", [SettingsScope.Project](SettingsScope.Project.html));  
      
                // Automatically extract all keywords from the Styles.
                provider.keywords = GetSearchKeywordsFromGUIContentProperties<Styles>();
                return provider;
            }  
      
            // [Settings](CameraEditor.Settings.html) [Asset](VersionControl.Asset.html) doesn't exist yet; no need to display anything in the [Settings](CameraEditor.Settings.html) window.
            return null;
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

