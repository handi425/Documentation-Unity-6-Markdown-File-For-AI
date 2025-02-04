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

#  [SearchIndexer](Search.SearchIndexer.html).name

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

public string name;

### Description

Name of the index. Generally this name is set by a user from
SearchDatabase.Settings.

    
    
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    /// <summary>
    /// The index name can be used to manage multiple indexes.
    /// </summary>
    static class Example_SearchIndexer_name
    {
        interface IItem
        {
            string name { get; }
            string stats { get; }
        }
    
        struct Weapon : IItem
        {
            public string name { get; set; }
            public int power { get; private set; }
    
            public string stats => $"Weapon Power {power}";
    
            public Weapon(string name, int power)
            {
                this.name = name;
                this.power = power;
            }
        }
    
        struct Armor : IItem
        {
            public string name { get; set; }
            public int defense { get; private set; }
    
            public string stats => $"Armor Defense {defense}";
    
            public Armor(string name, int defense)
            {
                this.name = name;
                this.defense = defense;
            }
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/name")]
        public static void Run()
        {
            var indexes = new[] { new [SearchIndexer](Search.SearchIndexer.html)(nameof(Weapon)), new [SearchIndexer](Search.SearchIndexer.html)(nameof(Armor)) };
    
            foreach (var i in indexes)
                i.Start();
    
            AddItem(indexes, new Weapon("Short Sword", 3));
            AddItem(indexes, new Weapon("Long Sword", 4));
            AddItem(indexes, new Armor("Ring", 1));
            AddItem(indexes, new Armor("Plate", 10));
    
            foreach (var i in indexes)
            {
                var localIndex = i;
                i.Finish(() =>
                {
                    OnIndexReady(localIndex);
                    localIndex.Dispose();
                });
            }
        }
    
        private static void AddItem(IEnumerable<[SearchIndexer](Search.SearchIndexer.html)> indexes, IItem item)
        {
            // Find the item indexer by matching the item type to the index name
            var itemIndexer = indexes.First(e => e.name == item.GetType().Name);
            var di = itemIndexer.AddDocument(item.name, checkIfExists: true);
            itemIndexer.AddProperty("stats", item.stats, di);
        }
    
        private static void OnIndexReady([SearchIndexer](Search.SearchIndexer.html) si)
        {
            string items = "";
            for (int di = 0; di < si.documentCount; ++di)
                items += si.GetDocument(di).id + ", ";
            [Debug.Log](Debug.Log.html)($"{si.name} index items {string.Join(", ", items)}");
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

