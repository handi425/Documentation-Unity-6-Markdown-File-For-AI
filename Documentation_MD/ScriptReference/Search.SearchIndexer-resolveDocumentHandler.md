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

#  [SearchIndexer](Search.SearchIndexer.html).resolveDocumentHandler

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

public Func<string,string> resolveDocumentHandler;

### Description

Handler used to resolve a document ID to some other data string.

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    /// <summary>
    /// Since the search indexes only contain string document IDs that must be unique,
    /// you can use `resolveDocumentHandler` to transform these document IDs into something
    /// that can be searched while running queries that contain simple words.
    /// </summary>
    static class Example_SearchIndexer_resolveDocumentHandler
    {
        struct Weapon
        {
            public string id { get; private set; }
            public int power { get; set; }
            public string name { get; set; }
    
            public Weapon(string name, int power)
            {
                id = System.Guid.NewGuid().ToString("N");
                this.name = name;
                this.power = power;
            }
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/resolveDocumentHandler")]
        public static void Run()
        {
            const int MagicPower = 1;
            var weapons = new[]
            {
                new Weapon("Long Bow", 2),
                new Weapon("Short Sword", 3),
                new Weapon("Short Sword", 3 + MagicPower), // We have two weapons that will have different ids, but the same name.
                new Weapon("Long Sword", 4)
            };
            var si = new [SearchIndexer](Search.SearchIndexer.html)("Weapons")
            {
                // Define a handler that returns a searchable string that can search for each document.
                // These words are not indexed, therefore the string is linear and might not scale as expected.
                // IMPORTANT: Unless you want to have case-sensitive search, you should convert the resolved string to lowercase.
                resolveDocumentHandler = (id) => weapons.First(w => w.id == id).name.ToLowerInvariant()
            };
    
            si.Start();
            foreach (var w in weapons)
            {
                var di = si.AddDocument(w.id);
                si.AddWord("weapon", 0, di);
            }
            si.Finish(() =>
            {
                OnIndexReady(si, weapons);
                // Dispose the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                si.Dispose();
            });
        }
    
        private static void OnIndexReady([SearchIndexer](Search.SearchIndexer.html) si, Weapon[] weapons)
        {
            var results = si.Search("weapon sword").ToArray();
            [Debug.Assert](Debug.Assert.html)(results.Length == 3, "No weapon were found");
            foreach (var result in results)
            {
                var w = weapons.First(w => w.id == result.id);
                [Debug.Log](Debug.Log.html)($"Found [{result.index}] {result.id}/{w.name} ({w.power})");
            }
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

