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

# AssetSettingsProvider

class in UnityEditor

/

Inherits from:[SettingsProvider](SettingsProvider.html)

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

AssetSettingsProvider is a specialization of the
[SettingsProvider](SettingsProvider.html) class that converts legacy settings
to Unified Settings. Legacy settings include any settings that used the
Inspector to modify themselves, such as the *.asset files under the
ProjectSettings folder. Under the hood, AssetSettingsProvider creates an
[Editor](Editor.html) for specific Assets and builds the UI for the Settings
window by wrapping the [Editor.OnInspectorGUI](Editor.OnInspectorGUI.html)
function.  
  
Internally we use this class to wrap our existing settings.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // Create a new type of [Settings](CameraEditor.Settings.html) [Asset](VersionControl.Asset.html).
    class MyCustomSettings : [ScriptableObject](ScriptableObject.html)
    {
        public const string k_MyCustomSettingsPath = "Assets/[Editor](Editor.html)/MyCustomSettings.asset";  
      
        [[SerializeField](SerializeField.html)]
        private int m_Number;  
      
        [[SerializeField](SerializeField.html)]
        private string m_SomeString;  
      
        internal static [SerializedObject](SerializedObject.html) GetSettings()
        {
            var settings = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<MyCustomSettings>(k_MyCustomSettingsPath);
            if (settings == null)
            {
                settings = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MyCustomSettings>();
                settings.m_Number = 42;
                settings.m_SomeString = "The answer to the universe";
                [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(settings, k_MyCustomSettingsPath);
            }  
      
            return new [SerializedObject](SerializedObject.html)(settings);
        }
    }  
      
    [[CustomEditor](CustomEditor.html)(typeof(MyCustomSettings))]
    class MyCustomSettingsEditor : [Editor](Editor.html)
    {
        // Nothing to do, this uses the Generic [Editor](Editor.html) to display MyCustomSettings properties
    }  
      
    class AssetSettingsProviderRegister
    {
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateFromFilePath()
        {
            // Create an [AssetSettingsProvider](AssetSettingsProvider.html) from a file path:
            var provider = [AssetSettingsProvider.CreateProviderFromAssetPath](AssetSettingsProvider.CreateProviderFromAssetPath.html)("Project/AssetSettings/FromFile", MyCustomSettings.k_MyCustomSettingsPath);  
      
            // Register keywords from the properties of MyCustomSettings
            provider.keywords = [SettingsProvider.GetSearchKeywordsFromSerializedObject](SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new [SerializedObject](SerializedObject.html)([AssetDatabase.LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html)(MyCustomSettings.k_MyCustomSettingsPath)));
            return provider;
        }  
      
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateFromSettingsObject()
        {
            // Create an [AssetSettingsProvider](AssetSettingsProvider.html) from a settings object (UnityEngine.Object):
            var settingsObj = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath);
            var provider = [AssetSettingsProvider.CreateProviderFromObject](AssetSettingsProvider.CreateProviderFromObject.html)("Project/AssetSettings/FromObject", settingsObj);  
      
            // Register keywords from the properties of MyCustomSettings
            provider.keywords = [SettingsProvider.GetSearchKeywordsFromSerializedObject](SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new [SerializedObject](SerializedObject.html)(settingsObj));
            return provider;
        }  
      
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateFromSettingsFromFunctor()
        {
            // Create an [AssetSettingsProvider](AssetSettingsProvider.html) from a functor that must return a UnityEngine.Object:
            var provider = new [AssetSettingsProvider](AssetSettingsProvider.html)("Project/AssetSettings/FromFunctor", () => [Editor.CreateEditor](Editor.CreateEditor.html)([AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath)));  
      
            // Register keywords from the properties of MyCustomSettings
            provider.keywords = [SettingsProvider.GetSearchKeywordsFromSerializedObject](SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new [SerializedObject](SerializedObject.html)([AssetDatabase.LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html)(MyCustomSettings.k_MyCustomSettingsPath)));
            return provider;
        }
    }
    

### Properties

[settingsEditor](AssetSettingsProvider-settingsEditor.html)| Editor providing
UI to modify the settings.  
---|---  
  
### Constructors

[AssetSettingsProvider](AssetSettingsProvider-ctor.html)| Creates a new
AssetSettingsProvider so you can wrap legacy settings (that is, settings that
previously appeared in the Inspector).  
---|---  
  
### Public Methods

[OnActivate](AssetSettingsProvider.OnActivate.html)| Overrides
SettingsProvider.OnActivate for this AssetSettingsProvider.  
---|---  
[OnDeactivate](AssetSettingsProvider.OnDeactivate.html)| Overrides
SettingsProvider.OnDeactivate for this AssetSettingsProvider.  
[OnFooterBarGUI](AssetSettingsProvider.OnFooterBarGUI.html)| Overrides
SettingsProvider.OnFooterBarGUI for this AssetSettingsProvider.  
[OnGUI](AssetSettingsProvider.OnGUI.html)| Overrides SettingsProvider.OnGUI
for this AssetSettingsProvider.  
[OnTitleBarGUI](AssetSettingsProvider.OnTitleBarGUI.html)| Overrides
SettingsProvider.OnTitleBarGUI for this AssetSettingsProvider. This draws the
button bar that contains the "add to preset" and the "help" buttons.  
  
### Static Methods

[CreateProviderFromAssetPath](AssetSettingsProvider.CreateProviderFromAssetPath.html)|
Create an AssetSettingsProvider from an asset path.  
---|---  
[CreateProviderFromObject](AssetSettingsProvider.CreateProviderFromObject.html)|
Create an AssetSettingsProvider from a settings object.  
[CreateProviderFromResourcePath](AssetSettingsProvider.CreateProviderFromResourcePath.html)|
Create an AssetSettingsProvider from an asset resource path.  
  
### Inherited Members

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
  
### Public Methods

[HasSearchInterest](SettingsProvider.HasSearchInterest.html)| Checks whether
the SettingsProvider should appear when the user types something in the
Settings window search box. SettingsProvider tries to match the search terms
(even partially) to any of the SettingsProvider.keywords. The search is case
insensitive.  
---|---  
[OnInspectorUpdate](SettingsProvider.OnInspectorUpdate.html)|
OnInspectorUpdate is called at 10 frames per second to give the inspector a
chance to update. See EditorWindow.OnInspectorUpdate for more details.  
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

