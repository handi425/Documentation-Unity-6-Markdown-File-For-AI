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

# ObjectSelectorEngineAttribute

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

Use this class attribute to register ObjectSelector search engines
automatically. Search engines with this attribute must implement the
[IObjectSelectorEngine](SearchService.IObjectSelectorEngine.html) interface.

The following example creates an ObjectSelector search engine:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEditor.SearchService;
    using Object = UnityEngine.Object;
    
    [ObjectSelectorEngine]
    class TestObjectSelectorSearchEngine : [IObjectSelectorEngine](SearchService.IObjectSelectorEngine.html)
    {
        public string name => "My Custom Engine";
    
        public void BeginSession([ISearchContext](SearchService.ISearchContext.html) context)
        {
        }
    
        public void EndSession([ISearchContext](SearchService.ISearchContext.html) context)
        {
            // EndSession can be called in two ways:
            // 1. Naturally when the onObjectSelectorClosed is called upon closing the window (which you should do in your window).
            // 2. Forcefully when a new session is started before the current one is finished.
            // In the second case, we need to close the window to avoid any issues since the ObjectSelector API does not support concurrent selectors.
            if (((([ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html))context).endSessionModes & [ObjectSelectorSearchEndSessionModes.CloseSelector](SearchService.ObjectSelectorSearchEndSessionModes.CloseSelector.html)) != 0 && ObjectSelectorWindow.instance != null)
            {
                ObjectSelectorWindow.instance.Close();
            }
        }
    
        public void BeginSearch([ISearchContext](SearchService.ISearchContext.html) context, string query)
        {
            // Not called.
        }
    
        public void EndSearch([ISearchContext](SearchService.ISearchContext.html) context)
        {
            // Not called.
        }
    
        public bool SelectObject([ISearchContext](SearchService.ISearchContext.html) context, [Action](Unity.Android.Gradle.Manifest.Action.html)<Object, bool> onObjectSelectorClosed, [Action](Unity.Android.Gradle.Manifest.Action.html)<Object> onObjectSelectedUpdated)
        {
            ObjectSelectorWindow.Show(([ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html))context, onObjectSelectedUpdated, onObjectSelectorClosed);
            return true;
        }
    
        public void SetSearchFilter([ISearchContext](SearchService.ISearchContext.html) context, string searchFilter)
        {
            ObjectSelectorWindow.instance.searchText = searchFilter;
        }
    }
    

The following example creates an object selector window that displays returned
items as a list of names and paths:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SearchService;
    using UnityEditor.UIElements;
    using UnityEngine.UIElements;
    using Object = UnityEngine.Object;
    
    public class ObjectSelectorWindow : [EditorWindow](EditorWindow.html)
    {
        public class ItemInfo
        {
            public int instanceId;
            public string label;
            public bool isAsset;
            public [GlobalObjectId](GlobalObjectId.html) globalObjectId;
        }
    
        static [ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html) s_Context;
        static [Action](Unity.Android.Gradle.Manifest.Action.html)<Object> s_OnSelectionChanged;
        static [Action](Unity.Android.Gradle.Manifest.Action.html)<Object, bool> s_OnSelectorClosed;
        public static ObjectSelectorWindow instance { get; private set; }
    
        List<ItemInfo> m_FilteredItems;
        [ToolbarSearchField](UIElements.ToolbarSearchField.html) m_Searchbox;
        [ListView](UIElements.ListView.html) m_ListView;
        string m_SearchText;
        ItemInfo m_CurrentItem;
        bool m_Canceled = true;
    
        public bool initialized { get; private set; } = false;
    
        public string searchText
        {
            get => m_SearchText;
            set
            {
                m_SearchText = value;
                FilterItems();
            }
        }
    
        public List<ItemInfo> allItems { get; private set; }
    
        public static void Show([ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html) context, [Action](Unity.Android.Gradle.Manifest.Action.html)<Object> onSelectionChanged, [Action](Unity.Android.Gradle.Manifest.Action.html)<Object, bool> onSelectorClosed)
        {
            s_Context = context;
            s_OnSelectionChanged = onSelectionChanged;
            s_OnSelectorClosed = onSelectorClosed;
    
            // Create a window with CreateInstance, and show it.
            var window = CreateInstance<ObjectSelectorWindow>();
            instance = window;
            window.Show();
        }
    
        void Init()
        {
            m_SearchText = "";
            allItems = new List<ItemInfo>();
            m_FilteredItems = new List<ItemInfo>();
    
            if ((s_Context.visibleObjects & [VisibleObjects.Assets](SearchService.VisibleObjects.Assets.html)) == [VisibleObjects.Assets](SearchService.VisibleObjects.Assets.html))
                allItems.AddRange(FetchAllAssets());
            if ((s_Context.visibleObjects & [VisibleObjects.Scene](SearchService.VisibleObjects.Scene.html)) == [VisibleObjects.Scene](SearchService.VisibleObjects.Scene.html))
                allItems.AddRange(FetchAllGameObjects(s_Context));
    
            allItems.Sort((item, other) => item.label.CompareTo(other.label));
            m_FilteredItems.AddRange(allItems);
        }
    
        void OnEnable()
        {
            Init();
    
            m_Searchbox = new [ToolbarSearchField](UIElements.ToolbarSearchField.html)();
            m_Searchbox.RegisterValueChangedCallback(SearchFilterChanged);
            m_Searchbox.style.flexGrow = 1;
            m_Searchbox.style.maxHeight = 16;
            m_Searchbox.style.width = [Length.Percent](UIElements.Length.Percent.html)(100f);
            m_Searchbox.style.marginRight = 4;
            rootVisualElement.Add(m_Searchbox);
    
            m_ListView = new [ListView](UIElements.ListView.html)(m_FilteredItems, 16, MakeItem, BindItem);
            m_ListView.selectionChanged += ItemSelectionChanged;
            m_ListView.itemsChosen += ItemsChosen;
            m_ListView.style.flexGrow = 1;
            rootVisualElement.Add(m_ListView);
    
            // Initialize selection
            if (s_Context.currentObject != null)
            {
                var currentSelectedId = s_Context.currentObject.GetInstanceID();
                var selectedIndex = m_FilteredItems.FindIndex(item => item.instanceId == currentSelectedId);
                if (selectedIndex >= 0)
                    m_ListView.selectedIndex = selectedIndex;
            }
    
            FinishInit();
        }
    
        void FinishInit()
        {
            [EditorApplication.delayCall](EditorApplication-delayCall.html) += () =>
            {
                m_ListView.Focus();
                initialized = true;
            };
        }
    
        void OnDisable()
        {
            // Call the onSelectorClosed callback when the window is closing.
            s_OnSelectorClosed?.Invoke(GetCurrentObject(), m_Canceled);
            instance = null;
        }
    
        void SearchFilterChanged(ChangeEvent<string> evt)
        {
            searchText = evt.newValue;
        }
    
        void FilterItems()
        {
            m_FilteredItems.Clear();
            m_FilteredItems.AddRange(allItems.Where(item => string.IsNullOrEmpty(searchText) || item.label.IndexOf(searchText, StringComparison.InvariantCultureIgnoreCase) >= 0));
    
            m_ListView.Rebuild();
        }
    
        void BindItem([VisualElement](UIElements.VisualElement.html) listItem, int index)
        {
            if (index < 0 || index >= m_FilteredItems.Count)
                return;
    
            var label = listItem as [Label](UIElements.Label.html);
            if (label == null)
                return;
            label.text = m_FilteredItems[index].label;
        }
    
        static [VisualElement](UIElements.VisualElement.html) MakeItem()
        {
            return new [Label](UIElements.Label.html)();
        }
    
        void ItemSelectionChanged(IEnumerable<object> selectedItems)
        {
            m_CurrentItem = selectedItems.FirstOrDefault() as ItemInfo;
            s_OnSelectionChanged?.Invoke(GetCurrentObject());
        }
    
        void ItemsChosen(IEnumerable<object> selectedItems)
        {
            m_CurrentItem = selectedItems.FirstOrDefault() as ItemInfo;
            m_Canceled = false;
            Close();
        }
    
        static IEnumerable<ItemInfo> FetchAllAssets()
        {
            var allPaths = AssetDatabase.GetAllAssetPaths();
            if (allPaths == null)
                yield break;
    
            var requiredTypes = s_Context.requiredTypeNames != null ? s_Context.requiredTypeNames.ToList() : new List<string>();
            foreach (var path in allPaths)
            {
                var type = [AssetDatabase.GetMainAssetTypeAtPath](AssetDatabase.GetMainAssetTypeAtPath.html)(path);
                var typeName = type.FullName ?? "";
                if (requiredTypes.Any(requiredType => typeName.Contains(requiredType)))
                {
                    var asset = [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(path);
                    var globalObjectId = [GlobalObjectId.GetGlobalObjectIdSlow](GlobalObjectId.GetGlobalObjectIdSlow.html)(asset);
                    var instanceId = asset?.GetInstanceID() ?? 0;
                    yield return new ItemInfo { instanceId = instanceId, label = path, isAsset = true, globalObjectId = globalObjectId };
                }
            }
        }
    
        static IEnumerable<ItemInfo> FetchAllGameObjects([ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html) context)
        {
            var property = new HierarchyProperty(HierarchyType.GameObjects, false);
    
            var requiredTypes = s_Context.requiredTypeNames != null ? s_Context.requiredTypeNames.ToList() : new List<string>();
            while (property.Next(null))
            {
                var objectReferenced = property.pptrValue;
                if (objectReferenced == null)
                    continue;
                var globalObjectId = [GlobalObjectId.GetGlobalObjectIdSlow](GlobalObjectId.GetGlobalObjectIdSlow.html)(property.instanceID);
                var typeName = objectReferenced.GetType().FullName ?? "";
                if (requiredTypes.Any(requiredType => typeName.Contains(requiredType)))
                    yield return new ItemInfo { instanceId = property.instanceID, label = property.name, isAsset = false, globalObjectId = globalObjectId };
            }
        }
    
        Object GetCurrentObject()
        {
            if (m_CurrentItem == null)
                return null;
            var currentInstanceId = m_CurrentItem.instanceId;
            if (m_CurrentItem.isAsset)
            {
                var asset = [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(m_CurrentItem.label);
                currentInstanceId = asset.GetInstanceID();
            }
            return [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(currentInstanceId);
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

