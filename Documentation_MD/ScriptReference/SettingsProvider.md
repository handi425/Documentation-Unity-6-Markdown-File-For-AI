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

# SettingsProvider

class in UnityEditor

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

SettingsProvider is the configuration class that specifies how a Project
setting or a preference should appear in the Settings or Preferences window.

In order to add new Project settings or preference pages, define a
SettingsProvider. The SettingsProvider class provides the hooks to display any
UI (using either IMGUI or UIElements to draw it). It also provides an API that
allows you to specify keywords which are used in the Settings and Preferences
windows in two ways:  
  
1) The search bar filters out SettingsProviders that don't have matching
keywords.  
  
2) Property Labels are highlighted with matching keywords.  
  
This example demonstrates multiple ways to create and configure different
SettingsProviders:

    
    
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;
    using UnityEditor.UIElements;  
      
    // Create a new type of [Settings](CameraEditor.Settings.html) [Asset](VersionControl.Asset.html).
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
    

### Properties

[activateHandler](SettingsProvider-activateHandler.html)| Overrides
SettingsProvider.OnActivate.  
---|---  
[deactivateHandler](SettingsProvider-deactivateHandler.html)| Overrides
SettingsProvider.OnDeactivate.  
[footerBarGuiHandler](SettingsProvider-footerBarGuiHandler.html)| Overrides
SettingsProvider.OnFooterBarGUI.  
[guiHandler](SettingsProvider-guiHandler.html)| Overrides
SettingsProvider.OnGUI.  
[hasSearchInterestHandler](SettingsProvider-hasSearchInterestHandler.html)|
Overrides SettingsProvider.HasSearchInterest.  
[inspectorUpdateHandler](SettingsProvider-inspectorUpdateHandler.html)|
Overrides SettingsProvider.OnInspectorUpdate.  
[keywords](SettingsProvider-keywords.html)| Gets or sets the list of keywords
to compare against what the user is searching for. When the user enters values
in the search box on the Settings window, SettingsProvider.HasSearchInterest
tries to match those keywords to this list.  
[label](SettingsProvider-label.html)| Gets or sets the display name of the
SettingsProvider as it appears in the Settings window. If not set, the
Settings window uses last token of SettingsProvider.settingsPath instead.  
[scope](SettingsProvider-scope.html)| Gets the Scope of the SettingsProvider.
The Scope determines whether the SettingsProvider appears in the Preferences
window (SettingsScope.User) or the Settings window (SettingsScope.Project).  
[settingsPath](SettingsProvider-settingsPath.html)| Gets Path used to place
the SettingsProvider in the tree view of the Settings window. The path should
be unique among all other settings paths and should use "/" as its separator.  
[titleBarGuiHandler](SettingsProvider-titleBarGuiHandler.html)| Overrides
SettingsProvider.OnTitleBarGUI.  
  
### Constructors

[SettingsProvider](SettingsProvider-ctor.html)| Creates a new
SettingsProvider.  
---|---  
  
### Public Methods

[HasSearchInterest](SettingsProvider.HasSearchInterest.html)| Checks whether
the SettingsProvider should appear when the user types something in the
Settings window search box. SettingsProvider tries to match the search terms
(even partially) to any of the SettingsProvider.keywords. The search is case
insensitive.  
---|---  
[OnActivate](SettingsProvider.OnActivate.html)| Use this function to implement
a handler for when the user clicks on the Settings in the Settings window. You
can fetch a settings Asset or set up UIElements UI from this function.  
[OnDeactivate](SettingsProvider.OnDeactivate.html)| Use this function to
implement a handler for when the user clicks on another setting or when the
Settings window closes.  
[OnFooterBarGUI](SettingsProvider.OnFooterBarGUI.html)| Use this function to
override drawing the footer for the SettingsProvider using IMGUI.  
[OnGUI](SettingsProvider.OnGUI.html)| Use this function to draw the UI based
on IMGUI. This assumes you haven't added any children to the rootElement
passed to the OnActivate function.  
[OnInspectorUpdate](SettingsProvider.OnInspectorUpdate.html)|
OnInspectorUpdate is called at 10 frames per second to give the inspector a
chance to update. See EditorWindow.OnInspectorUpdate for more details.  
[OnTitleBarGUI](SettingsProvider.OnTitleBarGUI.html)| Use this function to
override drawing the title for the SettingsProvider using IMGUI. This allows
you to add custom UI (such as a toolbar button) next to the title.
AssetSettingsProvider uses this mecanism to display the "add to preset" and
the "help" buttons.  
[Repaint](SettingsProvider.Repaint.html)| Request the SettingsWindow for a
repaint.  
  
### Static Methods

[GetSearchKeywordsFromGUIContentProperties](SettingsProvider.GetSearchKeywordsFromGUIContentProperties.html)|
Extract search keywords from all public static memebers in a specific Type.  
---|---  
[GetSearchKeywordsFromPath](SettingsProvider.GetSearchKeywordsFromPath.html)|
Extract search keywords from the serialized properties of an Asset at a
specific path.  
[GetSearchKeywordsFromSerializedObject](SettingsProvider.GetSearchKeywordsFromSerializedObject.html)|
Extract search keywords from from the serialized properties of a
SerializedObject.  
  
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

