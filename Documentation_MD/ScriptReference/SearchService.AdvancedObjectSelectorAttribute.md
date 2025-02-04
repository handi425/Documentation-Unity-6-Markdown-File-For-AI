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

# AdvancedObjectSelectorAttribute

class in UnityEditor.SearchService

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

This attribute lets you register a custom advanced object selector.

An advanced object selector is an object selector that can be customized
programatically to be opened on specific object fields, without modifying the
object fields themselves. It also allows total control over the UI, so you can
create your own search window if you wish to. There are two methods that need
to be registered: the object selector handler and the validator. The handler
opens the object selector, and the validator validates that the object
selector can be opened for the current selection
[context](SearchService.ObjectSelectorSearchContext.html). Here is an example
using [Search](Search.SearchService.ShowPicker.html) to open a custom object
selector only for materials:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Linq;
    using UnityEditor.Search;
    using UnityEditor.SearchService;
    using UnityEngine;
    
    static class MaterialSelector
    {
        const string MaterialSelectorId = "material_selector";
        static [ISearchView](Search.ISearchView.html) s_SearchView;
    
        [AdvancedObjectSelectorValidator(MaterialSelectorId)]
        static bool HandleAdvancedObjectSelectorValidation([ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html) context)
        {
            // This selector only works for assets.
            if ((context.visibleObjects & [VisibleObjects.Assets](SearchService.VisibleObjects.Assets.html)) == 0)
                return false;
    
            // This selector only supports materials and their derived types.
            if (!OnlyMaterialTypes(context))
                return false;
    
            return true;
        }
    
        [AdvancedObjectSelector(MaterialSelectorId, "[Material](Material.html) Selector", 10)]
        static void HandleAdvancedObjectSelector([AdvancedObjectSelectorEventType](SearchService.AdvancedObjectSelectorEventType.html) eventType, in [AdvancedObjectSelectorParameters](SearchService.AdvancedObjectSelectorParameters.html) parameters)
        {
            switch (eventType)
            {
                case [AdvancedObjectSelectorEventType.BeginSession](SearchService.AdvancedObjectSelectorEventType.BeginSession.html):
                    BeginSession(parameters);
                    break;
                case [AdvancedObjectSelectorEventType.EndSession](SearchService.AdvancedObjectSelectorEventType.EndSession.html):
                    EndSession(parameters);
                    break;
                case [AdvancedObjectSelectorEventType.SetSearchFilter](SearchService.AdvancedObjectSelectorEventType.SetSearchFilter.html):
                    SetSearchFilter(parameters);
                    break;
                case [AdvancedObjectSelectorEventType.OpenAndSearch](SearchService.AdvancedObjectSelectorEventType.OpenAndSearch.html):
                    OpenSelector(parameters);
                    break;
            };
        }
    
        static void BeginSession(in [AdvancedObjectSelectorParameters](SearchService.AdvancedObjectSelectorParameters.html) parameters)
        {
            // Here you can cache some data if needed.
        }
    
        static void EndSession(in [AdvancedObjectSelectorParameters](SearchService.AdvancedObjectSelectorParameters.html) parameters)
        {
            // Here you can clear the cached data if needed.
            // EndSession can be called in two ways:
            // 1. Naturally when the selectorClosedHandler is called upon closing the window (which you should do in your window if you don't use Search).
            // 2. Forcefully when a new session is started before the current one is finished.
            // In the second case, we need to close the window to avoid any issues since the ObjectSelector API does not support concurrent selectors.
            if ((parameters.context.endSessionModes & [ObjectSelectorSearchEndSessionModes.CloseSelector](SearchService.ObjectSelectorSearchEndSessionModes.CloseSelector.html)) != 0)
            {
                s_SearchView?.Close();
            }
    
            s_SearchView = null;
        }
    
        static void SetSearchFilter(in [AdvancedObjectSelectorParameters](SearchService.AdvancedObjectSelectorParameters.html) parameters)
        {
            // Here you can handle the request to set a new search filter.
            s_SearchView?.SetSearchText(parameters.searchFilter);
        }
    
        static void OpenSelector(in [AdvancedObjectSelectorParameters](SearchService.AdvancedObjectSelectorParameters.html) parameters)
        {
            var selectContext = parameters.context;
            var selectorCloseHandler = parameters.selectorClosedHandler;
            var trackingHandler = parameters.trackingHandler;
    
            // This selector handles any kind of materials, but if a specific material type is passed
            // in the context, then only this type of material will be shown.
            var searchText = string.Join(" or ", selectContext.requiredTypeNames.Select(typeName => $"t={typeName}"));
            var searchContext = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("asset", searchText);
            var viewState = [SearchViewState.CreatePickerState](Search.SearchViewState.CreatePickerState.html)("[Material](Material.html)",
                searchContext,
                selectHandler: (item, canceled) => selectorCloseHandler(item?.ToObject(), canceled),
                trackingHandler: (item) => trackingHandler(item?.ToObject()), null);
            viewState.windowTitle = new [GUIContent](GUIContent.html)("[Material](Material.html) Selector");
            viewState.position = [SearchUtils.GetMainWindowCenteredPosition](Search.SearchUtils.GetMainWindowCenteredPosition.html)(new [Vector2](Vector2.html)(600, 400));
            s_SearchView = [SearchService.ShowPicker](Search.SearchService.ShowPicker.html)(viewState);
        }
    
        static bool OnlyMaterialTypes([ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html) context)
        {
            var requiredTypes = context.requiredTypes.Zip(context.requiredTypeNames, (type, name) => new Tuple<Type, string>(type, name));
            return requiredTypes.All(typeAndName =>
            {
                return typeAndName.Item1 != null && typeof([Material](Material.html)).IsAssignableFrom(typeAndName.Item1) ||
                    typeAndName.Item2.Contains("material", StringComparison.OrdinalIgnoreCase);
            });
        }
    }
    

The signature of the method registered with the attribute
[AdvancedObjectSelectorAttribute](SearchService.AdvancedObjectSelectorAttribute.html)
must be the following:

    
    
    static void HandleAdvancedObjectSelector([AdvancedObjectSelectorEventType](SearchService.AdvancedObjectSelectorEventType.html) eventType, in [AdvancedObjectSelectorParameters](SearchService.AdvancedObjectSelectorParameters.html) parameters)
    

The signature of the method registered with the attribute
[AdvancedObjectSelectorValidatorAttribute](SearchService.AdvancedObjectSelectorValidatorAttribute.html)
must be the following:

    
    
    static bool HandleAdvancedObjectSelectorValidation([ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html) context)
    

**Note** : Those custom advanced object selectors are only active when the
Object Selector Engine is set to "Advanced" (see **Preferences/Search**
settings page).

### Constructors

[AdvancedObjectSelectorAttribute](SearchService.AdvancedObjectSelectorAttribute-
ctor.html)| Registers a method to act as an advanced object selector.  
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

