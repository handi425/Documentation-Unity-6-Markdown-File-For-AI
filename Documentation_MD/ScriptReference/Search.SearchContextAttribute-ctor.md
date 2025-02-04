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

# SearchContextAttribute Constructor

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

public SearchContextAttribute(string query);

## Declaration

public SearchContextAttribute(string query,
[Search.SearchViewFlags](Search.SearchViewFlags.html) flags);

## Declaration

public SearchContextAttribute(string query, string providerIdsCommaSeparated);

## Declaration

public SearchContextAttribute(string query, string providerIdsCommaSeparated,
[Search.SearchViewFlags](Search.SearchViewFlags.html) flags);

## Declaration

public SearchContextAttribute(string query, params Type[]
instantiableProviders);

## Declaration

public SearchContextAttribute(string query,
[Search.SearchViewFlags](Search.SearchViewFlags.html) flags, params Type[]
instantiableProviders);

## Declaration

public SearchContextAttribute(string query,
[Search.SearchViewFlags](Search.SearchViewFlags.html) flags, string
providerIdsCommaSeparated, params Type[] instantiableProviders);

### Parameters

query | Initial search query text used to open the Object Picker window.  
---|---  
flags | Search view flags used to open the Object Picker in various states.  
providerIdsCommaSeparated | A list of Search Provider IDs that will be used to create the search context.  
instantiableProviders | Search provider concrete types that will be instantiated and assigned to the Object Picker search context.  
  
### Description

Search context constructor used to add some search context to an object field.

    
    
    const string assetProviders = "adb;asset";
    const string objectProviders = "adb,asset,scene";
    const [SearchViewFlags](Search.SearchViewFlags.html) pickerMinimalUIFlags = [SearchViewFlags.Packages](Search.SearchViewFlags.Packages.html) |
        [SearchViewFlags.IgnoreSavedSearches](Search.SearchViewFlags.IgnoreSavedSearches.html) |
        [SearchViewFlags.DisableSavedSearchQuery](Search.SearchViewFlags.DisableSavedSearchQuery.html) |
        [SearchViewFlags.OpenInBuilderMode](Search.SearchViewFlags.OpenInBuilderMode.html) |
        [SearchViewFlags.DisableBuilderModeToggle](Search.SearchViewFlags.DisableBuilderModeToggle.html) |
        [SearchViewFlags.IgnoreSavedSearches](Search.SearchViewFlags.IgnoreSavedSearches.html);
    
    [[SearchContext](Search.SearchContext.html)("cub", "adb", [SearchViewFlags.ObjectPickerAdvancedUI](Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | [SearchViewFlags.ListView](Search.SearchViewFlags.ListView.html) | [SearchViewFlags.IgnoreSavedSearches](Search.SearchViewFlags.IgnoreSavedSearches.html))] public [MonoScript](MonoScript.html) myProjectScript;
    [[SearchContext](Search.SearchContext.html)("script", "adb", [SearchViewFlags.Packages](Search.SearchViewFlags.Packages.html) | [SearchViewFlags.CompactView](Search.SearchViewFlags.CompactView.html))] public [MonoScript](MonoScript.html) myPackageScript;
    [[SearchContext](Search.SearchContext.html)("t:texture", assetProviders, [SearchViewFlags.ObjectPickerAdvancedUI](Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | [SearchViewFlags.GridView](Search.SearchViewFlags.GridView.html))] public [Texture](Texture.html) myTexture;
    [[SearchContext](Search.SearchContext.html)("t:texture", assetProviders, [SearchViewFlags.ObjectPickerAdvancedUI](Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | [SearchViewFlags.GridView](Search.SearchViewFlags.GridView.html))] public [Texture](Texture.html)[] myTextureArray;
    [[SearchContext](Search.SearchContext.html)("t:texture", assetProviders, [SearchViewFlags.ObjectPickerAdvancedUI](Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | [SearchViewFlags.GridView](Search.SearchViewFlags.GridView.html))] public List<[Texture](Texture.html)> myTextureList;
    [[SearchContext](Search.SearchContext.html)("t:texture", "adb", [SearchViewFlags.OpenInspectorPreview](Search.SearchViewFlags.OpenInspectorPreview.html))] public [Texture](Texture.html) myTextureWithInspector;
    [[SearchContext](Search.SearchContext.html)("non_mobile", [SearchViewFlags.Centered](Search.SearchViewFlags.Centered.html))] public UnityEngine.Object myAnyObject;
    [[SearchContext](Search.SearchContext.html)("non_mobile", [SearchViewFlags.Debug](Search.SearchViewFlags.Debug.html))] public UnityEngine.Object myDebugObject;
    [[SearchContext](Search.SearchContext.html)("t:mesh is:nested mesh", "asset")] public UnityEngine.Object assetMesh;
    [[SearchContext](Search.SearchContext.html)("h: cube", "scene")] public [MeshFilter](MeshFilter.html) sceneMesh;
    [[SearchContext](Search.SearchContext.html)("shader:standard", assetProviders, [SearchViewFlags.HideSearchBar](Search.SearchViewFlags.HideSearchBar.html))] public [Material](Material.html) materialNoSearchBar;
    [[SearchContext](Search.SearchContext.html)("select{p:t:material, @label, @size}", objectProviders, [SearchViewFlags.TableView](Search.SearchViewFlags.TableView.html))] public [Material](Material.html) selectMaterial;
    [[SearchContext](Search.SearchContext.html)("Assets/[Queries](Unity.Android.Gradle.Manifest.Queries.html)/textures.asset", assetProviders)] public [Texture](Texture.html) searchQueryPathTexture;
    [[SearchContext](Search.SearchContext.html)("3c7f5dff3fb5d724688dfcecfb131b2a", assetProviders)] public [Texture](Texture.html) searchQueryGuidTexture;
    [[SearchContext](Search.SearchContext.html)("non_mobile", [SearchViewFlags.ObjectPickerAdvancedUI](Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | [SearchViewFlags.EnableSearchQuery](Search.SearchViewFlags.EnableSearchQuery.html))] public UnityEngine.Object myObjectWithSearchQueryEnabled;
    [[SearchContext](Search.SearchContext.html)("non_mobile", [SearchViewFlags.ObjectPickerAdvancedUI](Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | [SearchViewFlags.DisableInspectorPreview](Search.SearchViewFlags.DisableInspectorPreview.html))] public UnityEngine.Object myObjectWithInspectorDisabled;
    [[SearchContext](Search.SearchContext.html)("p: t:texture", "asset", [SearchViewFlags.ObjectPickerAdvancedUI](Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | [SearchViewFlags.OpenInBuilderMode](Search.SearchViewFlags.OpenInBuilderMode.html))] public [Texture](Texture.html) myTextureWithBuilder;
    [[SearchContext](Search.SearchContext.html)("p: t:texture", "asset", [SearchViewFlags.OpenInBuilderMode](Search.SearchViewFlags.OpenInBuilderMode.html) | [SearchViewFlags.DisableBuilderModeToggle](Search.SearchViewFlags.DisableBuilderModeToggle.html))] public [Texture](Texture.html) myTextureWithBuilderNoToggle;
    [[SearchContext](Search.SearchContext.html)("p: t:texture", "asset", [SearchViewFlags.OpenInTextMode](Search.SearchViewFlags.OpenInTextMode.html) | [SearchViewFlags.DisableBuilderModeToggle](Search.SearchViewFlags.DisableBuilderModeToggle.html))] public [Texture](Texture.html) myTextureNoBuilderNoToggle;
    [[SearchContext](Search.SearchContext.html)("t:currentobject{@type, 'texture'}", "asset")] public UnityEngine.Object myObjectWithContext;
    
    [[SearchContext](Search.SearchContext.html)("light")] public UnityEngine.GameObject lightSearch;
    [[SearchContext](Search.SearchContext.html)("camera", [SearchViewFlags.None](Search.SearchViewFlags.None.html))] public UnityEngine.GameObject cameraSearch;
    
    public UnityEngine.GameObject noSearchContext;
    
    #if USE_QUERY_BUILDER
    [[SearchContext](Search.SearchContext.html)("p: t:<$list:[Texture2D](Texture2D.html), [[Texture2D](Texture2D.html), [Material](Material.html), Prefab]$>", "asset", [SearchViewFlags.OpenInBuilderMode](Search.SearchViewFlags.OpenInBuilderMode.html) | [SearchViewFlags.DisableBuilderModeToggle](Search.SearchViewFlags.DisableBuilderModeToggle.html))] public UnityEngine.Object myObjectOfConstrainedTypes;
    #endif
    

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

