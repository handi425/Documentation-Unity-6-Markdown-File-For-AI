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

# SearchTable

class in UnityEditor.Search

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

A search table configuration is used to define the columns when search results
are displayed in table view.

See [DisplayMode.Table](Search.DisplayMode.Table.html).

    
    
    static [SearchTable](Search.SearchTable.html) CreateDecalsTableConfiguration()
    {
        var materialIcon = [EditorGUIUtility.Load](EditorGUIUtility.Load.html)("[Material](Material.html) Icon") as [Texture](Texture.html);
        var shaderIcon = [EditorGUIUtility.Load](EditorGUIUtility.Load.html)("[Shader](Shader.html) Icon") as [Texture](Texture.html);
        return new [SearchTable](Search.SearchTable.html)("decals", new [SearchColumn](Search.SearchColumn.html)[]
        {
            new [SearchColumn](Search.SearchColumn.html)("DecalsName0", "label", "name", new [GUIContent](GUIContent.html)("Name", materialIcon)) { width = 160 },
            new [SearchColumn](Search.SearchColumn.html)("DecalsShader1", "#shader", "name", new [GUIContent](GUIContent.html)("[Shader](Shader.html)", shaderIcon)) { width = 150 },
            new [SearchColumn](Search.SearchColumn.html)("DecalsBaseColor1", "#_BaseColor", "color", new [GUIContent](GUIContent.html)("[Color](Color.html)", shaderIcon)) { width = 130 },
        });
    }
    

The previous example can be used when creating a
[SearchViewState](Search.SearchViewState.html).

    
    
    var selectHandler = args.selectorClosedHandler;
    var trackingHandler = args.trackingHandler;
    
    var query = [SearchService.CreateContext](Search.SearchService.CreateContext.html)(CreateDecalProvider(), $"a={dbName} t={selectContext.requiredTypeNames.First()} shader=Decal");
    var viewState = [SearchViewState.CreatePickerState](Search.SearchViewState.CreatePickerState.html)("decals",
        query,
        selectHandler: (item, canceled) => selectHandler(item?.ToObject(), canceled),
        trackingHandler: (item) => trackingHandler(item?.ToObject()), null,
        [SearchViewFlags.TableView](Search.SearchViewFlags.TableView.html)
        );
    viewState.tableConfig = CreateDecalsTableConfiguration();
    var materialIcon = [EditorGUIUtility.Load](EditorGUIUtility.Load.html)("[Material](Material.html) Icon") as [Texture](Texture.html);
    viewState.windowTitle = new [GUIContent](GUIContent.html)("[Material](Material.html) Decals", materialIcon);
    viewState.hideAllGroup = true;
    viewState.position = [SearchUtils.GetMainWindowCenteredPosition](Search.SearchUtils.GetMainWindowCenteredPosition.html)(new [Vector2](Vector2.html)(600, 400));
    s_SearchView = [SearchService.ShowPicker](Search.SearchService.ShowPicker.html)(viewState);
    

### Properties

[columns](Search.SearchTable-columns.html)| Search columns displayed in table
view.  
---|---  
[id](Search.SearchTable-id.html)| Unique id of the search table used for
persistance.  
[name](Search.SearchTable-name.html)| Display name of the search table used
for serialization.  
  
### Constructors

[SearchTable](Search.SearchTable-ctor.html)| Creates a new search table
configuration.  
---|---  
  
### Public Methods

[Clone](Search.SearchTable.Clone.html)| Creates a copy of the search table
configuration.  
---|---  
[InitFunctors](Search.SearchTable.InitFunctors.html)| Initialize all search
columns functors based on their format provider.  
  
### Static Methods

[LoadFromFile](Search.SearchTable.LoadFromFile.html)| Load a search table
configuraiton from a JSON file.  
---|---  
  
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

