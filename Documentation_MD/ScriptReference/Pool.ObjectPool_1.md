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

# ObjectPool<T0>

class in UnityEngine.Pool

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

  

Implements interfaces:[IObjectPool<T0>](Pool.IObjectPool_1.html)

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

A stack based [IObjectPool<T0>](Pool.IObjectPool_1.html).

Object Pooling is a way to optimize your projects and lower the burden that is
placed on the CPU when having to rapidly create and destroy new objects. It is
a good practice and design pattern to keep in mind to help relieve the
processing power of the CPU to handle more important tasks and not become
inundated by repetitive create and destroy calls. The ObjectPool uses a stack
to hold a collection of object instances for reuse and is not thread-safe.

    
    
    using System.Text;
    using UnityEngine;
    using UnityEngine.Pool;  
      
    // This component returns the particle system to the pool when the OnParticleSystemStopped event is received.
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ReturnToPool : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ParticleSystem](ParticleSystem.html) system;
        public IObjectPool<[ParticleSystem](ParticleSystem.html)> pool;  
      
        void Start()
        {
            system = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var main = system.main;
            main.stopAction = [ParticleSystemStopAction.Callback](ParticleSystemStopAction.Callback.html);
        }  
      
        void OnParticleSystemStopped()
        {
            // Return to the pool
            pool.Release(system);
        }
    }  
      
    // This example spans a random number of ParticleSystems using a pool so that old systems can be reused.
    public class PoolExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public enum PoolType
        {
            Stack,
            LinkedList
        }  
      
        public PoolType poolType;  
      
        // Collection checks will throw errors if we try to release an item that is already in the pool.
        public bool collectionChecks = true;
        public int maxPoolSize = 10;  
      
        IObjectPool<[ParticleSystem](ParticleSystem.html)> m_Pool;  
      
        public IObjectPool<[ParticleSystem](ParticleSystem.html)> Pool
        {
            get
            {
                if (m_Pool == null)
                {
                    if (poolType == PoolType.Stack)
                        m_Pool = new ObjectPool<[ParticleSystem](ParticleSystem.html)>(CreatePooledItem, OnTakeFromPool, OnReturnedToPool, OnDestroyPoolObject, collectionChecks, 10, maxPoolSize);
                    else
                        m_Pool = new LinkedPool<[ParticleSystem](ParticleSystem.html)>(CreatePooledItem, OnTakeFromPool, OnReturnedToPool, OnDestroyPoolObject, collectionChecks, maxPoolSize);
                }
                return m_Pool;
            }
        }  
      
        [ParticleSystem](ParticleSystem.html) CreatePooledItem()
        {
            var go = new [GameObject](GameObject.html)("Pooled [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var ps = go.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            ps.Stop(true, [ParticleSystemStopBehavior.StopEmittingAndClear](ParticleSystemStopBehavior.StopEmittingAndClear.html));  
      
            var main = ps.main;
            main.duration = 1;
            main.startLifetime = 1;
            main.loop = false;  
      
            // This is used to return ParticleSystems to the pool when they have stopped.
            var returnToPool = go.AddComponent<ReturnToPool>();
            returnToPool.pool = Pool;  
      
            return ps;
        }  
      
        // Called when an item is returned to the pool using Release
        void OnReturnedToPool([ParticleSystem](ParticleSystem.html) system)
        {
            system.gameObject.SetActive(false);
        }  
      
        // Called when an item is taken from the pool using Get
        void OnTakeFromPool([ParticleSystem](ParticleSystem.html) system)
        {
            system.gameObject.SetActive(true);
        }  
      
        // If the pool capacity is reached then any items returned will be destroyed.
        // We can control what the destroy behavior does, here we destroy the [GameObject](GameObject.html).
        void OnDestroyPoolObject([ParticleSystem](ParticleSystem.html) system)
        {
            Destroy(system.gameObject);
        }  
      
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("Pool size: " + Pool.CountInactive);
            if ([GUILayout.Button](GUILayout.Button.html)("Create Particles"))
            {
                var amount = [Random.Range](Random.Range.html)(1, 10);
                for (int i = 0; i < amount; ++i)
                {
                    var ps = Pool.Get();
                    ps.transform.position = [Random.insideUnitSphere](Random-insideUnitSphere.html) * 10;
                    ps.Play();
                }
            }
        }
    }
    

### Properties

[CountActive](Pool.ObjectPool_1.CountActive.html)| Number of objects that have
been created by the pool but are currently in use and have not yet been
returned.  
---|---  
[CountAll](Pool.ObjectPool_1.CountAll.html)| The total number of active and
inactive objects.  
[CountInactive](Pool.ObjectPool_1.CountInactive.html)| Number of objects that
are currently available in the pool.  
  
### Constructors

[ObjectPool_1](Pool.ObjectPool_1-ctor.html)| Creates a new ObjectPool
instance.  
---|---  
  
### Public Methods

[Clear](Pool.ObjectPool_1.Clear.html)| Removes all pooled items. If the pool
contains a destroy callback then it will be called for each item that is in
the pool.  
---|---  
[Dispose](Pool.ObjectPool_1.Dispose.html)| Removes all pooled items. If the
pool contains a destroy callback then it will be called for each item that is
in the pool.  
[Get](Pool.ObjectPool_1.Get.html)| Get an instance from the pool. If the pool
is empty then a new instance will be created.  
[Release](Pool.ObjectPool_1.Release.html)| Returns the instance back to the
pool. Returning an instance to a pool that is full will cause the instance to
be destroyed.  
  
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

